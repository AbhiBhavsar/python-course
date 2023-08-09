from django.shortcuts import get_object_or_404, render
from .models import Post

all_posts = Post.objects.all()
# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, 'blog/index.html', {'latest_posts': latest_posts})


def posts(request):
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts
    })


def post_detail(request, slug):
    # detailed_post = Post.objects.get(slug=slug)
    detailed_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {'post': detailed_post, "post_tags":detailed_post.tags.all()})
