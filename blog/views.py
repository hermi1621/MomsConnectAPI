from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, PostForm
from .models import Post

@login_required(login_url='login')  # Only logged-in users can create posts
def home(request):
    posts = Post.objects.all().order_by('-created_at')  # show newest posts first
    form = PostForm()
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')  # refresh page after posting
    
    context = {
        'posts': posts,
        'form': form
    }
    return render(request, 'blog/home.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redirect to login after successful registration
    else:
        form = RegisterForm()
    
    return render(request, 'blog/register.html', {'form': form})
