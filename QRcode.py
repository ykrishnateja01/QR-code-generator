
pip install qrcode

import qrcode
def generate_qr_code(data, filename):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)

if _name_ == "_main_":
    # Get user input for the data to be encoded in the QR code
    data = input("Enter the data to be encoded in the QR code: ")

    # Get user input for the filename to save the QR code image
    filename = input("Enter the filename to save the QR code image with extension, e.g., my_qr_code.png: ")

    # Generate and save the QR code
    generate_qr_code(data, filename)

    print(f"QR code generated and saved as {filename}")

