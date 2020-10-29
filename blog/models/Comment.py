from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from blog.models import Post


class Comment(MPTTModel):
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,
                            on_delete=models.CASCADE)

    user_comment = models.CharField(max_length=500, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    # approved = models.BooleanField(default=False)

    class MPTTMeta:
        order_insertion_by = ['date_added']

    def __str__(self):
        return self.user_comment[:20]
