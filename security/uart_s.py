import serial
import subprocess

# Configure serial port
ser = serial.Serial('/dev/serial0', 115200, timeout=5)  # Replace ttyS0 with your UART port

# File to store the received certificate
with open("received_certificate.crt", "w") as file:
    while True:
        data = ser.readline().decode('utf-8')
        if data:
            file.write(data)
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


