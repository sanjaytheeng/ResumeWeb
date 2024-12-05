from django.shortcuts import render, redirect
from .forms import ResumeForm

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