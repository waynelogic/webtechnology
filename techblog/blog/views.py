from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Article

# Create your views here.
def home(request):
    # return HttpResponse('Hello, World')
    article = Article.objects.all()
    context = {
        'articles': article
    }
    return render(request, 'pages/home.html', context)

def about(request):
    # return HttpResponse('Hello, World')
    return render(request, 'pages/about.html')

def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    # return HttpResponse('Hello, World')
    return render(request, 'pages/article.html', {
        'article' : article
    })