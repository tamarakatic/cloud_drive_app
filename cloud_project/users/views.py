from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm
from .models import Document


def document_upload(request):
    if request.method == 'POST' and request.FILES.get('image_file', False):
        image_file = request.FILES['image_file']
        upload = Document(file=image_file)
        upload.save()
    documents = Document.objects.all()
    return render(request, 'users/profile.html', {'documents': documents})

def delete(request):
    if request.method == 'GET':
        parameter = request.GET.get("parameter")
        Document.objects.filter(file=parameter).delete()
        return redirect('profile')
  

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):    
    documents = Document.objects.all()
    return render(request, 'users/profile.html', {'documents': documents})
