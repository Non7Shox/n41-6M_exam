import random
from django.contrib.auth import logout, get_user_model

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from users.forms import RegistrationForm, LoginForm
from users.models import UserConfirmationModel
from config.settings import EMAIL_HOST_USER


def send_confirmation_email(email):
    subject = 'Confirmation your email'
    code = random.randint(1000, 9999)
    if UserConfirmationModel.objects.filter(email=email).exists():
        send_confirmation_email(email)
    emails = [email]
    from_email = EMAIL_HOST_USER
    if send_mail(subject=subject, message=str(code), from_email=from_email, recipient_list=emails):
        UserConfirmationModel.objects.create(
            email=email,
            code=code,
            is_active=True
        )
        return True
    else:
        return False


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.is_active = False
            user.save()
            if send_confirmation_email(email=form.cleaned_data['email']):
                return render(request, 'confirmation.html')
            else:
                return redirect('books:list')
        else:
            return HttpResponse(form.errors)
    else:
        return render(request, 'register.html')


def confirmation_view(request):
    if request.method == 'POST':
        code = request.POST['code']
        user_code = UserConfirmationModel.objects.get(code=code)
        if user_code:
            user = User.objects.get(email=user_code.email)
            user.is_active = True
            user.save()
            return redirect('users:login')
        else:
            return redirect('books:list')
    else:
        return render(request, 'confirmation.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('books:list')
            else:
                return render(request, 'login.html')
        else:
            return render(request, 'login.html', context={'form': form})
    else:
        form = LoginForm()  # Create an empty form for GET requests
    return render(request, 'login.html', context={'form': form})


def log_out_view(request):
    logout(request)
    # Redirect to a specific page after logout (optional)
    return redirect('logout')
