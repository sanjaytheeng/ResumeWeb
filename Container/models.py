from django.db import models

class Resume(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    linkedin_url = models.URLField(blank=True, null=True)
    skills = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"