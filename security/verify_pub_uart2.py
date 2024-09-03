import serial
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
import base64
import subprocess

import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import json
from datetime import datetime

mqtt_broker = "192.168.0.128"
mqtt_port = 1883
mqtt_topic = "pki/web"

GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
GPIO.setup(23, GPIO.OUT)  # Set GPIO 23 as an output pin
GPIO.setwarnings(False)
duration = 3  # Set the duration for how long GPIO 23 should stay high

def load_certificate(file_path):
    """Load a certificate from a PEM file."""
    with open(file_path, 'rb') as f:
        cert_data = f.read()
    return x509.load_pem_x509_certificate(cert_data, default_backend())

def verify_certificate_chain(device_cert_path, ca_certificates):
    """Verify the device certificate against a list of CA certificates."""
    # Load the device certificate
    device_certificate = load_certificate(device_cert_path)

    # Load the CA certificates
    ca_cert_objs = [load_certificate(ca_cert) for ca_cert in ca_certificates]
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="ECU-2")
    client.connect(mqtt_broker, mqtt_port, 60)

    # Start with the device certificate and check against each CA certificate
    for ca_cert in ca_cert_objs:
        try:
            # Use the CA's public key to verify the device certificate's signature
            ca_cert.public_key().verify(
                device_certificate.signature,
                device_certificate.tbs_certificate_bytes,
                padding.PKCS1v15(),  # Correct padding for RSA
                device_certificate.signature_hash_algorithm  # Hash algorithm used for signing
            )
            print(f"Device certificate '{device_cert_path}' is valid and trusted by '{ca_cert.subject}'.")
            GPIO.output(23, GPIO.HIGH)
            time.sleep(duration)
            GPIO.output(23, GPIO.LOW)

            #publishing data to dashboard
            # Data to send
            timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M")
            data = {
                "Vehicle ID": 1002,
                "deviceName": "ECU2",
                "Verify": True,
                "certName": "ECU2.crt",
                "rootCA": "rootCA",
                "interCA": "Intermediate CA",
                "timestamp": timestamp
            }
            json_data = json.dumps(data)
            # print(data)

            # Publish the JSON data
            client.publish(mqtt_topic, json_data)
            # Disconnect from the broker
            client.disconnect()

            return  # Exit the function if the certificate is verified successfully

        except Exception as e:
            print(f"Failed to verify device certificate with '{ca_cert.subject}': {e}")

    print("Device certificate verification failed: no valid certificate authority found.")
    # Data to send
    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M")
    data = {
        "Vehicle ID": 1002,
        "deviceName": "ECU2",
        "Verify": False,
        "certName": "ECU2.crt",
        "rootCA": "outsideCA",
        "interCA": "outsideIntermediateCA",
        "timestamp": timestamp
    }
    json_data = json.dumps(data)
    
    client.publish(mqtt_topic, json_data)
    client.disconnect()
    

def receive_certificate_via_uart():
    # Configure serial port
    ser = serial.Serial('/dev/serial0', 115200, timeout=10)  # Replace ttyS0 with your UART port

    # File to store the received certificate
    with open("received_certificate.crt", "w") as file:
        while True:
            data = ser.readline()
            #time.sleep(1)
            if data:
                file.write(data.decode('utf-8'))
            else:
                break

    ser.close()

    # Verify if the file is a proper PEM file
    try:
        result = subprocess.run(['openssl', 'x509', '-in', 'received_certificate.crt', '-text', '-noout'],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print("Certificate is valid and correctly formatted!")
        else:
            print("There was an issue with the certificate formatting.")
            print(result.stderr.decode('utf-8'))
    except FileNotFoundError:
        print("OpenSSL is not installed on your system. Please install it to verify the certificate.")
    
    return 'received_certificate.crt'

if __name__ == "__main__":
    # Receive the certificate over UART
    device_cert_path = receive_certificate_via_uart()
    print(device_cert_path)

    # Paths to your CA certificates
    intermediate_ca_cert_path = 'intermediateCA.crt'
    server_cert_path = 'server.crt'

    # List of CA certificates for verification
    ca_certificates = [intermediate_ca_cert_path, server_cert_path]

    # Verify the device certificate if received successfully
    if device_cert_path:
        verify_certificate_chain(device_cert_path, ca_certificates)