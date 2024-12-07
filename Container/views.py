from django.shortcuts import render, redirect, get_object_or_404
from .forms import ResumeForm
from .models import Resume

def submit_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume_success') 
    else:
        form = ResumeForm()
    return render(request, 'container/resume.html', {'form': form})

def resume_success(request):
    return render(request, 'container/success.html')


def index(request):
    return render(request, 'container/home.html')

def edit_resume(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('resume_detail', resume_id=resume.id)  # Redirect to the resume detail page
    else:
        form = ResumeForm(instance=resume)  # Pre-fill the form with existing data
    
    return render(request, 'dashboard/edit_resume.html', {'form': form, 'resume': resume})