from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from apps.models import Category, Advert


def main_page(request):
    context = {
        'categories': Category.objects.all(),
        'adverts': Advert.objects.all()
    }
    return render(request, 'apps/main.html', context)


def category_detail(request, slug):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'apps/main.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('profile_page')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile_page')

    return render(request, 'apps/login.html')


def logout_page(request):
    logout(request)
    return redirect('main_page')


def register_page(request):
    if request.user.is_authenticated:
        return redirect('profile_page')

    if request.method == 'POST':
        print(request.POST)
        User.objects.create_user(
            first_name=request.POST.get('first_name'),
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
        )
        return redirect('login_page')

    return render(request, 'apps/register.html')


def profile_page(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login_page')

    return render(request, 'apps/profile.html')
