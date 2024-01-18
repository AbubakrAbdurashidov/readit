from django.shortcuts import render

from django.shortcuts import render

from .models import Article


def article_list_view(request):
    articles = Article.objects.order_by('-id')

    ctx = {

    }
    return render(request, 'article/blog.html', ctx)


def article_detail_view(request, slug):

    ctx = {

    }
    return render(request, 'article/blog-single.html', ctx)
