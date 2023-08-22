from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Signuplist
from .forms import loginlist
from django.core.mail import send_mail
from social_django.views import complete
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import connection
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from .models import AsmaEmail
from .models import User
import random
import string

def facebook_callback(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    try:
        user_social = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        user_social = None

    if user_social:
        pass
    else:
        user_social = user.social_auth.create(
            provider='facebook',
            uid=user.email,  
        )
        
        AsmaEmail.objects.create(email=user.email)
    
    return redirect('success')

from django.db import models


def home(request):
    return render(request,"MyApp/home.html",{})

def success (request):
    return render(request,"MyApp/success.html",{})


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def signup(request):
    if request.method == 'POST':
        form = Signuplist(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            username = generate_random_string(8)
            password = generate_random_string(10)

            user = User(name=name, lastname=lastname, email=email, phone=phone, username=username, password=password)
            user.save()

            if email:
                subject = 'تسجيل الدخول'
                message = f' username : {username}  password : {password}.'
                from_email = 'quiewquiew@gmail.com'
                recipient_list = [email]
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)

           
            email_data = {
                'name': name,
                'lastname': lastname,
                'email': email,
                'phone': phone,
                'username': username,
                'password': password,
            }
            print(email_data)
    else:
        form = Signuplist()

    return render(request, "MyApp/signup.html", {"form": form})



def login_view(request):
    if request.method == 'POST':
        form = loginlist(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT id FROM asma WHERE username = %s AND password = %s", [username, password])
                user_id = cursor.fetchone()
                
                if user_id:
                    user = {'id': user_id[0], 'username': username}  
                    request.session['user'] = user
                    return redirect('success')
                else:
                    return redirect('home')
    else:
        return render(request, 'MyApp/home.html', {})

