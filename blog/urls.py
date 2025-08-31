from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Home page – show posts and form to create posts
    path('', views.home, name='home'),

    # User registration
    path('register/', views.register, name='register'),

    # User login
    path('login/', auth_views.LoginView.as_view(
        template_name='blog/login.html'
    ), name='login'),

    # User logout
    path('logout/', auth_views.LogoutView.as_view(
        next_page='home'
    ), name='logout'),
]
