from configparser import ConfigParser, ExtendedInterpolation
import subprocess
import time


config = ConfigParser(interpolation=ExtendedInterpolation())

try:
    config.read("settings.ini")
except Exception as error:
    print(f"[Error ] : {error}")
    raise SystemExit()


def get_info(keys):

    # parameters
    country = config[keys]["country"]
    state = config[keys]["state"]
    location = config[keys]["location"]
    organization = config[keys]["organization"]
    common_name = config[keys]["common_name"]

    subject = f"/C={country}/ST={state}/L={location}/O={organization}/CN={common_name}"
    return subject


# function to generate certificates for Devices
def generate_client(device_name, client_name):
    subject_client = get_info(client_name)
    print(subject_client)

    cmd1 = f"openssl req -new -nodes -sha256 -subj '{subject_client}' -out {device_name}.csr -keyout {device_name}.key"
    subprocess.run(cmd1, shell=True)

    cmd2 = f"openssl x509 -req -sha256 -in {device_name}.csr -CA ./cdac_ca_server/ca.crt -CAkey ./cdac_ca_server/ca.key -CAcreateserial -out {device_name}.crt -days 365"
    subprocess.run(cmd2, shell=True)


# enter "certificate file name" and "settings options" as arguments
generate_client(device_name="rpi", client_name="Client2")
