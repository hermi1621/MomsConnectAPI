from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    return render(request, 'blog/home.html', {'posts': posts, 'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # after register → go to login
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})
