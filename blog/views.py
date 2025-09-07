from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm, PostForm
from .models import Post

# ---------------- HOME ----------------
@login_required(login_url='login')  # only logged-in users can access home
def home(request):
    posts = Post.objects.all().order_by('-created_at')  # newest first
    form = PostForm()
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')  # refresh page
    
    return render(request, 'blog/home.html', {'posts': posts, 'form': form})


# ---------------- REGISTER ----------------
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # go to login after signup
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})


# ---------------- EDIT POST ----------------
@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form})


# ---------------- DELETE POST ----------------
@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'blog/delete_post.html', {'post': post})


# ---------------- PROFILE ----------------
def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = user.posts.all().order_by('-created_at')  # using related_name='posts'
    return render(request, 'blog/profile.html', {'user_profile': user, 'posts': posts})
