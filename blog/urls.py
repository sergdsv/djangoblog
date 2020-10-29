
from django.urls import path
from .controllers import PostController, CategoryController, CommentController
urlpatterns = [

    path('', PostController.index, name='post-list'),
    path('post/<slug>/', PostController.show, name='post-detail'),
    path('category/<slug>/', PostController.category_show, name='category-show'),
    path('comment_add/<id>', CommentController.comment_add, name='comment-add')

]
