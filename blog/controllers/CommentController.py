from django.shortcuts import render, redirect
from django.http import HttpRequest
from blog.models import Post, Comment


def comment_add(request: HttpRequest, id):

    if request.method == 'POST':
        post = Post.objects.get(pk=id)
        comment = request._post['comment_text']
        comment_parent = post.comments.get(pk=request._post['comment_id'])
        Comment.objects.create(user_comment=comment, post=post, parent=comment_parent)
        return redirect('post-detail', slug=post.slug)
