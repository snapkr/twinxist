from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<article_id>[0-9]+)/$', views.article, name='article'),
    url(r'^bookmark/(?P<article_id>[0-9]+)/$', views.bookmark, name='bookmark'),
    url(r'^bookmark/(?P<article_id>[0-9]+)/project/(?P<category_id>[0-9]+)/$', views.bookmark_project, name='bookmark-project'),
    url(r'^bookmark/(?P<article_id>[0-9]+)/category/(?P<category_id>[0-9]+)/$', views.bookmark_category, name='bookmark-category'),
    url(r'^like/(?P<article_id>[0-9]+)/$', views.favorite, name='favorite')
]