from django.shortcuts import render, get_object_or_404
from Container.models import Resume
from django.http import HttpResponse
from django.template.loader import render_to_string


def dashboard(request):
    resumes = Resume.objects.all().order_by('-created_at')
    return render(request, 'dashboard/dashboard.html', {'resumes': resumes})

def resume_detail(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    return render(request, 'dashboard/resume_detail.html', {'resume': resume})

# def generate_pdf(request, resume_id):
#     resume = Resume.objects.get(id=resume_id)

#     html_content = render_to_string('dashboard/resume_detailed_pdf.html', {'resume': resume})

#     pdf = HTML(string=html_content).write_pdf()

#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="resume_{resume.first_name}_{resume.last_name}.pdf"'

#     return response