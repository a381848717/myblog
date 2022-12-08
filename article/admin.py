from django.contrib import admin
from .models import Article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_title', 'article_author', 'article_topic', 'status', 'create_date')

    '''filter options'''
    list_filter = ('status',)

    '''10 items per page'''
    list_per_page = 10


admin.site.register(Article, ArticleAdmin)