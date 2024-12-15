import qrcode
from io import BytesIO
import base64
from django.db import models
from django.utils.html import mark_safe

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    skills = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def generate_github_qrcode(self):
        """Generate a base64-encoded QR code for the GitHub URL."""
        if self.github_url:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(self.github_url)
            qr.make(fit=True)

            # Generate QR code image and encode it in base64
            img = qr.make_image(fill_color="black", back_color="white")
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            img_base64 = base64.b64encode(buffer.read()).decode('utf-8')
            return mark_safe(f'<img src="data:image/png;base64,{img_base64}" width="100"/>')
        return "No GitHub URL"
