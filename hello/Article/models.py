from django.db import models
from dynamic_scraper.models import Scraper, SchedulerRuntime
from scrapy.contrib.djangoitem import DjangoItem
from django.contrib.auth.models import User


class Website(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.TextField()
    
    def __unicode__(self):
        return self.name
        
class Project(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.TextField()
    
    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    news_website = models.ForeignKey(Website)
    description = models.TextField(blank=True)
    image = models.CharField(max_length=200, blank=None, null=True)
    url = models.URLField()
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)
    categories = models.ManyToManyField(Category, blank=True)
    projects = models.ManyToManyField(Project, blank=True)

    def __unicode__(self):
        return self.title


class ArticleItem(DjangoItem):
    django_model = Article
    
class Favorite(models.Model):
    user = models.ForeignKey(User, unique=False)
    article = models.ForeignKey(Article, unique=False, related_name='favorites')
