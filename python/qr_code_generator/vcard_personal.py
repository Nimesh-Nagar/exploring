import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
import os

# --- Final Optimized vCard ---
vcard = """BEGIN:VCARD
VERSION:3.0
FN:Nimesh Nagar
N:Nagar;Nimesh;;;
TEL;TYPE=CELL,VOICE:+91 90332 81629
EMAIL;TYPE=HOME:n.nimesh02@gmail.com
URL:www.linkedin.com/in/nimesh-nagar-47b6aa137
END:VCARD"""

# Create folder
dir_name = "QR_codes"
os.makedirs(dir_name, exist_ok=True)

# --- vCard QR ---
qr_vcard = qrcode.QRCode(
    version=3,
    box_size=6,
    border=2
)
qr_vcard.add_data(vcard)
qr_vcard.make(fit=True)

img_vcard = qr_vcard.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    fill_color="#0a3d62",    # dark blue
    back_color="#f5f6fa"     # soft white/gray
)
img_vcard.save(os.path.join(dir_name, "Nimesh_vCard.png"))


# --- LinkedIn QR ---
linkedin_url = "www.linkedin.com/in/nimesh-nagar-47b6aa137"

qr_linkedin = qrcode.QRCode(
    version=2,
    box_size=6,
    border=2
)
qr_linkedin.add_data(linkedin_url)
qr_linkedin.make(fit=True)

img_linkedin = qr_linkedin.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    fill_color="#0077B5",    # LinkedIn Blue
    back_color="white"
)
img_linkedin.save(os.path.join(dir_name, "Nimesh_LinkedIn.png"))

print("QR codes generated successfully in 'QR_codes' folder:")
print("- Nimesh_vCard.png  (Save contact)")
print("- Nimesh_LinkedIn.png (Open LinkedIn)")
