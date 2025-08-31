from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, PostForm
from .models import Post

# Home view: show posts and allow logged-in users to create posts
@login_required(login_url='login')  # Redirect to login if not logged in
def home(request):
    posts = Post.objects.all().order_by('-created_at')  # Show latest posts first
    form = PostForm()
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Link post to logged-in user
            post.save()
            return redirect('home')  # Refresh page to show new post

    return render(request, 'blog/home.html', {'posts': posts, 'form': form})

# Registration view: allow new users to sign up
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = RegisterForm()
    
    return render(request, 'blog/register.html', {'form': form})
