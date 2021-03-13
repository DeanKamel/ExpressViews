from django.contrib import admin
from .models import Article, Comment, Report


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'author', 'publish', 'topic'
    )
    list_filter = (
        'publish', 'likes', 'dislikes', 'topic'
    )
    search_fields = (
        'title', 'body'
    )
    prepopulated_fields = {
        'slug': ('title',)
    }
    raw_id_fields = (
        'author',
    )
    ordering = (
        'publish',
    )
    date_hierarchy = 'publish'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'body', 'created_on'
    )
    list_filter = (
        'name', 'created_on'
    )
    search_fields = (
        'name', 'body'
    )

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'reason'
    )


