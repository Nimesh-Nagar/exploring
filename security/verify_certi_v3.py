from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding

def load_certificate(file_path):
    """Load a certificate from a PEM file."""
    with open(file_path, 'rb') as f:
        cert_data = f.read()
    return x509.load_pem_x509_certificate(cert_data, default_backend())

def verify_certificate_chain(device_cert_path, ca_certificates):
    # Load the device certificate
    device_certificate = load_certificate(device_cert_path)

    # Load the CA certificates
    ca_cert_objs = [load_certificate(ca_cert) for ca_cert in ca_certificates]

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
            return  # Exit the function if the certificate is verified successfully
        except Exception as e:
            print(f"Failed to verify device certificate with '{ca_cert.subject}': {e}")

    print("Device certificate verification failed: no valid certificate authority found.")

if __name__ == "__main__":
    # Paths to your certificates
    # device_cert_path = 'iot_device.crt'
    device_cert_path = 'device.crt'

    intermediate_ca_cert_path = 'intermediateCA.crt'
    server_cert_path = 'server.crt'

    # List of CA certificates for verification
    ca_certificates = [intermediate_ca_cert_path, server_cert_path]

    # Verify the device certificate
    verify_certificate_chain(device_cert_path, ca_certificates)