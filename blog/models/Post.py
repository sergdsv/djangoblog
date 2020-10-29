from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
# from blog.models import Category


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE
    )
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'blog'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
