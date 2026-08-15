"""
qr_service.py - QR Code Generator Service for Agro-Medicines
Generates printable SVG/DataURI QR codes linking to usage guides and video tutorials.
"""

import urllib.parse

def generate_product_qr_code(product_id, product_name):
    """
    Generate Data URI QR Code URL pointing to product instruction page.
    """
    target_url = f"http://127.0.0.1:5000/product/{product_id}"
    encoded_url = urllib.parse.quote(target_url)
    # Return quick QR API image URL
    qr_image_url = f"https://api.qrserver.com/v1/create-qr-code/?size=160x160&data={encoded_url}"
    return {
        "qr_image_url": qr_image_url,
        "target_url": target_url
    }
