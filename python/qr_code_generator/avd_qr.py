from PIL import Image
import qrcode
import os

# Create a QR code object
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Define the data to be encoded in the QR code
data = "https://www.elementaliot.com/"

# Add the data to the QR code object
qr.add_data(data)

# Make the QR code
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color=(49,80,202), back_color=(198,206,240))

# Open the logo or image file
logo = Image.open("logo.png")

# Resize the logo or image if needed
logo = logo.resize((50, 50))

# Position the logo or image in the center of the QR code
img_w, img_h = img.size
logo_w, logo_h = logo.size
pos = ((img_w - logo_w) // 2, (img_h - logo_h) // 2)

# Paste the logo or image onto the QR code
img.paste(logo, pos)

# Save the QR code image with logo or image

dir_name = "QR_codes"
os.makedirs(dir_name, exist_ok=True)

path = os.path.join(dir_name, "qr_code_with_logo.png")

img.save(path)
