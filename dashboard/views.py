from django.shortcuts import render, get_object_or_404 # type: ignore
from Container.models import Resume
from django.http import HttpResponse # type: ignore
from django.conf import settings # type: ignore
import os
from reportlab.lib.units import inch
from reportlab.platypus import Image
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import qrcode
from io import BytesIO
from django.urls import reverse

def dashboard(request):
    resumes = Resume.objects.all().order_by('-created_at')
    return render(request, 'dashboard/dashboard.html', {'resumes': resumes})

def resume_detail(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    return render(request, 'dashboard/resume_detail.html', {'resume': resume})

def generate_pdf(request, resume_id):
    # Fetch the resume object from the database
    resume = get_object_or_404(Resume, id=resume_id)

    # Create a new HttpResponse object with PDF content type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="resume_{resume_id}.pdf"'  # Ensure PDF is downloaded as an attachment

    # Set up a SimpleDocTemplate to generate the PDF
    doc = SimpleDocTemplate(
        response,
        pagesize=letter,
        topMargin=50,
        bottomMargin=50,
        rightMargin=50,
        leftMargin=50
    )
    styles = getSampleStyleSheet()
    elements = []

    # Add Name Section
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(f"{resume.first_name} {resume.last_name}", styles['Title']))

    # Add Contact Information
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(f"Email: {resume.contact_email}", styles['Normal']))
    elements.append(Paragraph(f"Phone: {resume.phone_number}", styles['Normal']))
    elements.append(Paragraph(f"LinkedIn: {resume.linkedin_url}", styles['Normal']))

    # Skills Section
    elements.append(Spacer(1, 20))
    elements.append(Paragraph("Skills", styles['Heading2']))
    elements.append(Paragraph(resume.skills or "N/A", styles['Normal']))

    # Education Section
    elements.append(Spacer(1, 20))
    elements.append(Paragraph("Education", styles['Heading2']))
    elements.append(Paragraph(resume.education or "N/A", styles['Normal']))

    # Experience Section
    elements.append(Spacer(1, 20))
    elements.append(Paragraph("Experience", styles['Heading2']))
    elements.append(Paragraph(resume.experience or "N/A", styles['Normal']))

    # Build the PDF
    doc.build(elements)

    return response

def index(request):
    return render(request, 'dashboard/index.html')

def generate_resume_qr(request, resume_id):
    # Create the URL to the resume PDF

    # resume_pdf_url = request.build_absolute_uri(reverse('generate_pdf', args=[resume_id]))
    resume_pdf_url = "https://d414-2400-1a00-b050-a87-24c7-a4c2-30-451b.ngrok-free.app/resume/{resume_id}/generate_pdf/"


    # Generate the QR code from the PDF URL
    qr = qrcode.make(resume_pdf_url)
    
    # Save the QR code to memory
    img_io = BytesIO()
    qr.save(img_io)
    img_io.seek(0)
    
    # Return the QR code image in response
    return HttpResponse(img_io, content_type='image/png')

def errorpage(request):
    return render(request, 'system/404.html')

def sysregister(request):
    return render(request, 'system/register.html')

def content(request):
    return render(request, 'system/content.html')