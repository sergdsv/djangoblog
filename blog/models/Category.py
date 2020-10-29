from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.template.defaultfilters import slugify


class Category(MPTTModel):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True, null=True)
    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True,
                            related_name='children',
                            )

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        app_label = 'blog'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
