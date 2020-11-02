
from django.urls import path
from .controllers import PostController, CategoryController, CommentController, TestController
urlpatterns = [

    path('', PostController.index, name='home'),
    path('post/<slug>/', PostController.show, name='post-detail'),
    path('category/<slug>/', PostController.category_show, name='category-show'),
    path('comment_add/<id>', CommentController.comment_add, name='comment-add'),
    path('test/', TestController.test, name='test'),
    path('resume/', PostController.resume, name='resume')
]
