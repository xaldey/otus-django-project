from django.http import HttpResponse
from django.shortcuts import render

# from .models import Author, Article


def index_view(request):
    return HttpResponse('<h1>Hello, OtusPlus index!</h1>')

    # article = Article.objects.get(pk=3)
    # context = {
    #     'foo': 'bar',
    #     'article': article,
    #     'all_articles': Article.objects.all(),
    #     'all_B_authors': Author.objects.filter(first_name__startswith='B')
    #
    # }
    return render(request, 'otusPlus/index.html', context=context)
