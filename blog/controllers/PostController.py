from django.shortcuts import render
from blog.models import Post, Category


def index(request):
    posts = Post.objects.all().prefetch_related('category')
    categories = Category.objects.all()
    return render(
        request,
        'post_list.html',
        {
            'posts': posts,
            'categories': categories
        }
    )


def show(request, slug):
    post = Post.objects.get(slug=slug)
    categories = Category.objects.all()
    comments = post.comments.all()
    return render(
        request,
        'post_detail.html',
        {
            'post': post,
            'categories': categories,
            'comments': comments
         }
    )


def category_show(request, slug):
    category = Category.objects.get(slug=slug)
    categories = Category.objects.all()
    posts = Post.objects.filter(category=category.id).prefetch_related('category')
    return render(
        request,
        'post_list_category.html',
        {
            'posts': posts,
            'categories': categories
         }
    )
