from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),      # Home page
    path('posts/', views.posts, name='posts')  # Posts page
]
