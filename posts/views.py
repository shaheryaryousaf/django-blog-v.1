from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/all-posts.html', context)


def post(request, post_id):
    # 404 Error
	post = get_object_or_404(Post, pk=post_id)

	context = {
		'post': post
	}

	return render(request, 'posts/single.html', context)
