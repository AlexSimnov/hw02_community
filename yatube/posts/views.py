from django.shortcuts import get_object_or_404, render

from .models import Group, Post

PAGES: int = 10


def index(request):
    posts = Post.objects.all()[:PAGES]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def posts_list(request, slug):

    group = get_object_or_404(Group, slug=slug)

    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
