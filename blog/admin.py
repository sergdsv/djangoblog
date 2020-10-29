from django.contrib import admin
from .models import Post, Category, Comment
from mptt.admin import DraggableMPTTAdmin


class CategoryMPTTModelAdmin(DraggableMPTTAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20
    list_display = ('title', 'slug')


admin.site.register(Comment, DraggableMPTTAdmin)


class CommentMPTTModelAdmin(DraggableMPTTAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20
    list_display = ('user_comment', )


admin.site.register(Category, DraggableMPTTAdmin)


class ThingInline(admin.TabularInline):
    model = Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'created_date', 'published_date')
    ordering = ('title',)
    search_fields = ('title', 'slug')
    inlines = [
        ThingInline,
    ]



