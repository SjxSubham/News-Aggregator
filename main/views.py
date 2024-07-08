from django.shortcuts import render,redirect
from django.contrib import messages
from .models import News, Category, Comment
# example/views.py
from datetime import datetime

from django.http import HttpResponse


def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)

def home(request):
    first_news=News.objects.first()
    three_news=News.objects.all()[1:3]
    three_categories=Category.objects.all()[0:3]
    return render(request, 'home.html', {
        'first_news': first_news,
        'three_news': three_news,
        'three_categories':three_categories,
    })
# All news
def all_news(request):
    all_news=News.objects.all()
    return render(request, 'all-news.html',{
        'all_news':all_news
    })
        
#detail
def detail(request,id):
    news=News.objects.get(pk=id)
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        comment=request.POST['message']
        Comment.objects.create(
            news=news,
            name=name,
            comment=comment
        )
        messages.succes(request,'Comment is succesfully added')
    category=Category.objects.get(id=news.category.id)
    rel_news=News.objects.filter(category=category).exclude(id=id)
    comments=Comment.objects.filter(news=news,status=True).order_by('-id')
    return render(request, 'detail.html',{
        'detail':news,
        'related_news':rel_news,
        'comments':comments
    })
# Fetch
def all_category(request):
    cats=Category.objects.all()
    return render(request, 'category.html',{
        'cats':cats
    })
#fetch all category
def category(request,id):
    category=Category.objects.get(id=id)
    news=News.objects.filter(category=category)
    return render(request, 'category-news.html',{
        'all_news':news,
        'category':category
    })
