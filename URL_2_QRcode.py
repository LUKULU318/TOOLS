import qrcode

# Function to convert URL to QR code
def url_to_qr(url, file_name='url_qr.png'):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
        box_size=10,  # size of each box
        border=4,  # thickness of the border
    )
    
    # Add URL to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the generated QR code as an image file
    img.save(file_name)
    print(f"QR code for URL generated and saved as {file_name}")

# Example usage
url = "https://www.example.com"
url_to_qr(url, 'example_url_qr.png')
