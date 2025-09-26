from django.urls import path

from apps.views import main_page, register_page, login_page, profile_page, logout_page, category_detail

urlpatterns = [
    path('', main_page, name='main_page'),
    path('register', register_page, name='register_page'),
    path('login', login_page, name='login_page'),
    path('profile', profile_page, name='profile_page'),
    path('logout', logout_page, name='logout_page'),
    path('<slug:slug>', category_detail, name='category_detail'),
]
