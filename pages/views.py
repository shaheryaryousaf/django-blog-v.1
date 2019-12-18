from django.shortcuts import render
from posts.models import Post

def index(request):
    posts = Post.objects.order_by('-create_date')[:5]
    context = {
        'posts': posts
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def contact_us(request):
    return render(request, 'pages/contact.html')