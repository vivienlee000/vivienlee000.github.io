from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Issue

import os
# Create your views here.
def index(request):
    # latest_article = Article.objects.order_by('date')[:1]
    # latest_issue = Article.objects.order_by('date')[:1]

    # context = {
    #     "latest_article": latest_article,
    #     "latest_issue": latest_issue
    # }
    return render(request, 'sections/index.html', {})
    # return HttpResponse("lol")



def about(request):
    return render(request, 'sections/about.html', {})

# def issues(request):
#     context = {}
#     return render(request, 'sections/issues.html', context)
#
# def articles(request):
#     context = {}
#     return render(request, 'sections/articles.html', context)

# def article(request, article_id):
#     context = {}
#     return render(request, 'sections/articles/' % article_id, {})
