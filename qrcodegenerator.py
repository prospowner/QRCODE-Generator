# qrcode generator

import os
import qrcode


def generate_qr_code():
    print("--- Python QR Code Generator ---")

    # 1. Get input from the user
    url = input("Enter the text or URL you want to encode: ").strip()
    if not url:
        print("Error: Input cannot be empty!")
        return

    filename = input("Enter the output filename: ").strip()
    if not filename:
        filename = "qrcode_output.png"
    if not filename.endswith(".png"):
        filename += ".png"

    # 2. Configure the QR Code looks and size and design
    qr = qrcode.QRCode(
        version=1,  
        error_correction=qrcode.constants.ERROR_CORRECT_M,  
        box_size=10,  
        border=4,  
    )

    try:
       
        qr.add_data(url) 
        qr.make(fit=True)

        # 4. Generate and save the image
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)

        print(
            f"\nSuccess! Your QR code has been saved as: {os.path.abspath(filename)}"
        )

    except Exception as e:
        print(f"An error occurred while generating the QR code: {e}")


if __name__ == "__main__":
    generate_qr_code()