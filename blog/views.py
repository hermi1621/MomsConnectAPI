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
