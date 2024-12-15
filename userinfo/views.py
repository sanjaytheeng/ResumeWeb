from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserForm
from .models import User
import qrcode
from io import BytesIO
from userinfo.forms import UserForm
import base64
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.http import JsonResponse




def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your details have been submitted successfully!")
            return redirect('user_form')
    else:
        form = UserForm()
    return render(request, 'userinfo/user_form.html', {'form': form})

def admin_view(request):
    users = User.objects.all()
    return render(request, 'userinfo/admin_view.html', {'users': users})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, "User has been deleted successfully!")
    return redirect('admin_view')

def home_page(request):
    users = User.objects.all()
    return render(request, 'userinfo/home_page.html', {'users': users})

def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'userinfo/user_detail.html', {'user': user})

def generate_pdf(request, user_id):
    user = get_object_or_404(User, id=user_id)
    template = get_template('userinfo/user_detail_pdf.html')
    html = template.render({'user': user})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{user.first_name}_{user.last_name}_Resume.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def chatbot_response(request):
    user_message = request.GET.get('message', '')
    # Example simple responses (replace with logic or API calls for advanced chatbot)
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how to add a student": "Click on the 'Add Student' button on the home page to add a new student.",
        "what is this app": "This app helps manage Student information and generate resumes.",
        "thank you": "It's my pleasure!",
        "phone number of sanskar": "748274572.",
        "phone number of pranish": "9840724609.",
        "phone number of sanjay": "9748274572.",
        "phone number of shreenarayan": "9861619561.",
        "phone number of nemo": "9818138857.",
        "phone number of Bhishma": "9804958637.",
    }
    response = responses.get(user_message.lower(), "Sorry, I didn't understand that. Can you rephrase?")
    return JsonResponse({'response': response})