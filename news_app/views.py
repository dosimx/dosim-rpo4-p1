from urllib.request import Request

from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.db.models import Q
import re

def home_page(request):
    hot_posts = Post.objects.all().order_by('-created_at')[:4]
    posts = Post.objects.all()

    context = {
        'hot_posts': hot_posts,
        'posts': posts,
    }

    return render(request, 'index.html', context)

def news_by_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category).order_by('-created_at')
    context = {
        'category': category,
        'posts' : posts,
    }

    return render(request, 'news-by-category.html', context)

def search_page(request):
    return render(request, 'search.html')

def search_results(request):
    query = (request.GET.get('q') or '').strip()
    results = []

    if query:
        pattern = re.escape(query)  # экранируем спецсимволы
        results = Post.objects.filter(
            Q(title__iregex=pattern) | Q(content__iregex=pattern)
        )

    context = {
        'query': query,
        'results': results,
    }

    return render(request, 'search-results.html', context)

def read_news_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post' : post,
    }
    return render(request, 'read-news.html', context)