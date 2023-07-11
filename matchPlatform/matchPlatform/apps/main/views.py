from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def file(request):
    with open('/app/text.txt', 'r') as file:
        file_content = file.read()

    return HttpResponse(file_content, content_type='text/plain')

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')

            if password == confirm_password:
                CustomUser.objects.create_user(username=username, password=password)
                return redirect('login')
            else:
                # You can add an error message to indicate that the passwords do not match
                form.add_error('confirm_password', 'Passwords do not match')

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        nickname = request.POST['nickname']
        password = request.POST['password']
        user = authenticate(request, username=nickname, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')


@login_required
def profile(request):
    username = request.user.username
    ctx = {'username':username}
    return render(request, 'profile.html', ctx)