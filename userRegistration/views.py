from django.shortcuts import render, redirect
# from .models import UserRegistrationModel
from .forms import ResistrationForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def user_registration(request):
    form = ResistrationForm()
    if request.method == 'POST':
        first_name      = request.POST.get('first_name')
        last_name       = request.POST.get('last_name')
        username        = request.POST.get('username')
        email           = request.POST.get('email')
        password        = request.POST.get('password2')

        user = User.objects.create_user(first_name=first_name, last_name=last_name,username=username, email=email, password=password)
        user.save()
        print('user created')
        return redirect('/login/')

    return render(request, 'user-registration.html', {'registration_form': form})


def user_login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect('/')
        else:
            return redirect('/login/')
    return render(request, 'user-login.html', {'login_form': form})

# @login_required(login_url='/login/', redirect_field_name='/')
def home(request):
    username = request.user.username

    if not request.user.is_authenticated:
        print('user is authenticated')
    return render(request, 'index.html', {'username': username})
