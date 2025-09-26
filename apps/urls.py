from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.views import main_page, register_page, login_page, profile_page, logout_page

urlpatterns = [
    path('', main_page, name='main_page'),
    path('register', register_page, name='register_page'),
    path('login', login_page, name='login_page'),
    path('profile', profile_page, name='profile_page'),
    path('logout', logout_page, name='logout_page'),
]
