from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from haystack.query import SearchQuerySet
from Article import models
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
@login_required
def article(request, article_id):
    artikel = models.Article.objects.get(id = article_id)
    related = SearchQuerySet().more_like_this(artikel)
    template = loader.get_template('content/article/article.html')
    context = RequestContext(request, {
        'artikel': artikel,
        'related': related
    })
    return HttpResponse(template.render(context))

@login_required
def bookmark(request, article_id):
    template = loader.get_template('content/bookmark/add_bookmark_form.html')
    context = {
        'article': models.Article.objects.get(id = article_id),
        'categories': models.Category.objects.all(),
        'projects': models.Project.objects.all(),
    }
    return HttpResponse(template.render(context))

@login_required
def bookmark_category(request, article_id, category_id):
    article = models.Article.objects.get(id = article_id)
    category = models.Category.objects.get(id = category_id)
    article.categories.add(category)
    data = {}

    return HttpResponse(json.dumps(data), content_type="application/json")

@login_required
def bookmark_project(request, article_id, project_id):
    article = models.Article.objects.get(id = article_id)
    project = models.Project.objects.get(id = project_id)
    article.projects.add(project)

    return HttpResponse(json.dumps(data), content_type="application/json")


@login_required
def favorite(request, article_id):
    article = models.Article.objects.get(id = article_id)
    data = {}
    favorites = models.Favorite.objects.filter(article = article, user= request.user)
    if (not favorites):
        favorite = models.Favorite(article = article, user= request.user)
        favorite.save()
        data['liked'] = True
    else:
        data['liked'] = False
        favorites.delete()

    data['likes'] = models.Favorite.objects.filter(article=article).count()
    return HttpResponse(json.dumps(data), content_type="application/json")

@login_required
def index(
        request,
        template='content/article/articleList.html',
        page_template='content/article/articleList_page.html'):
    context = {
        'artikelen': models.Article.objects.all(),
        'favorites': models.Favorite.objects.all(),
        'favorited': [article.article for article in models.Favorite.objects.filter(user=request.user.id)],
        'user': request.user,
        'page_template': page_template,
    }
    if request.is_ajax():
        template = page_template
    return render_to_response(
        template, context, context_instance=RequestContext(request))