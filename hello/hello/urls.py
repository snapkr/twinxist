from django.conf.urls import include, url
from django.contrib import admin
import Article.views


urlpatterns = [
    # Examples:
    # url(r'^$', 'testSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('Article.urls')),
    #url(r'^$', Article.views.index, name='index'),
    #url(r'^(?P<article_id>[0-9]+)/$', Article.views.article, name='article'),
    url(r'^article/', include('Article.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^search/', include('haystack.urls'))

]
