import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

# Create a QR code object
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Define the WiFi data
wifi = "WIFI:S:CDAC2.4-AP15;T:WPA;P:CdacDelta@#321;;"

# Add the WiFi data to the QR code object
qr.add_data(wifi)
qr.make(fit=True)

# Create the QR code image
img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# Define text label
label = "Scan QR-Code to Connect WiFi"

# Get image dimensions
img_width, img_height = img.size

# Load a font (default PIL font or a TTF if you have one)
try:
    font = ImageFont.truetype("arial.ttf", 20)
except IOError:
    font = ImageFont.load_default()

# Use textbbox to calculate text size
dummy_img = Image.new("RGB", (1, 1))
dummy_draw = ImageDraw.Draw(dummy_img)
text_bbox = dummy_draw.textbbox((0, 0), label, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# Create a new image with extra space for the label
new_img = Image.new("RGB", (img_width, img_height + text_height + 20), "white")
new_img.paste(img, (0, 0))

# Draw the text centered
draw = ImageDraw.Draw(new_img)
text_position = ((img_width - text_width) // 2, img_height + 15)
draw.text(text_position, label, fill="black", font=font)

# Save the final image
dir_name = "QR_codes"
os.makedirs(dir_name, exist_ok=True)

path = os.path.join(dir_name, "qr_code_wifi_labeled.png")

new_img.save(path)

