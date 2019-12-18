from django.shortcuts import render, get_object_or_404
from posts.models import Post
from .models import Category

def index(request, category_id):
    posts = Post.objects.all().filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)

    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'categories/category.html', context)
