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


from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('post/edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('post/delete/<int:pk>/', views.delete_post, name='delete_post'),
]


path('profile/<str:username>/', views.profile, name='profile'),

