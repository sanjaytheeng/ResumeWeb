from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            'first_name', 'last_name', 'photo', 'contact_email', 
            'phone_number', 'linkedin_url', 'skills', 
            'education', 'experience'
        ]
