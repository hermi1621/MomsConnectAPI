from django.shortcuts import render

def home(request):
    return render(request, 'blog/base.html')

def posts(request):
    return render(request, 'blog/base.html')



from django.shortcuts import render

def home(request):
    return render(request, 'blog/base.html')  # Your HTML page

def posts(request):
    return render(request, 'blog/base.html')  # Can be same page for now

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, PostForm
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/base.html', {'posts': posts, 'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})
