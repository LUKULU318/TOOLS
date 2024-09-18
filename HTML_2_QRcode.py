import qrcode

# Function to convert HTML to QR code
def html_to_qr(html_content, file_name='html_qr.png'):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
        box_size=10,  # size of each box
        border=4,  # thickness of the border
    )
    
    # Add HTML content to the QR code
    qr.add_data(html_content)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the generated QR code as an image file
    img.save(file_name)
    print(f"QR code generated and saved as {file_name}")

# Example usage
html_content = """
<html>
<head><title>Test HTML</title></head>
<body>
<h1>Hello, World!</h1>
<p>This is a test HTML content in a QR code.</p>
</body>
</html>
"""
html_to_qr(html_content, 'html_qr.png')
