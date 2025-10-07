# ref.  https://medium.com/@rahulmallah785671/create-qr-code-by-using-python-2370d7bd9b8d


import qrcode


'''
here are four error correction levels available: 
L (low), M (medium), Q (quartile), and H (high). 
The higher the error correction level, the more data can be recovered if the QR code is damaged.
'''

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=5,
)
qr.add_data('https://www.elementaliot.com/')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("qr_code.png")
