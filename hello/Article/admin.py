from django.contrib import admin

# Register your models here.
from .models import Website, Article, Category, Project, Favorite

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'news_website', 'url', 'date', 'time')
    list_filter = ('news_website', 'date')
    search_fields = ['description']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Website)
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Favorite)
