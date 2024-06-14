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
    
    #parameters 
    country = config[keys]["country"]
    state = config[keys]["state"]
    location = config[keys]["location"]
    organization = config[keys]["organization"]
    common_name = config[keys]["common_name"]

    subject = f"/C={country}/ST={state}/L={location}/O={organization}/CN={common_name}"
    return subject 


#Function to generate the Root CA 
def generate_root_ca():
    subject_ca = get_info("Root CA")
    
    print(subject_ca)
    cmd1 = f"openssl req -x509 -nodes -sha256 -newkey rsa:2048 -subj '{subject_ca}' -days 365 -keyout ca.key -out ca.crt" 
    subprocess.run(cmd1, shell=True)
 
#Function to generate server certificats
def generate_server():
    subject_server = get_info("Server")
    print(subject_server)
    
    cmd2= f"openssl req -nodes -sha256 -new -subj '{subject_server}' -keyout server.key -out server.csr"
    subprocess.run(cmd2, shell=True)
    
    cmd3 = f"openssl x509 -req -sha256 -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 365"
    subprocess.run(cmd3, shell=True)
 
generate_root_ca()
time.sleep(1)
generate_server()
