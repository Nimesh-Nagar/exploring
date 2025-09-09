import qrcode
import os

# Create a QR code object
qr = qrcode.QRCode(version=1, box_size=5, border=5)

# Define the vCard data
vcard = """BEGIN:VCARD
VERSION:4.0
FN:Nimesh Nagar
ORG:Elemental IoT
TITLE:CEO
TEL;TYPE=WORK,VOICE:+91 90332 81629
EMAIL;TYPE=PREF,INTERNET:info@elementaliot.com
URL:https://www.elementaliot.com
END:VCARD"""

# Add the vCard data to the QR code object
qr.add_data(vcard)

# Make the QR code
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the vcard QR code to image

dir_name = "QR_codes"
os.makedirs(dir_name, exist_ok=True)

path = os.path.join(dir_name, "Nimesh_vcard.png")

img.save(path)
