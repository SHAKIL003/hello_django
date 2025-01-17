from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
# Create your views here.

posts = [
    {
        'author': 'Shakil Ahmad',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 01, 2025'
    },
    {
        'author': 'Sajjad Qari',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 10, 2025'
    }
]

context = {
    'posts': Post.objects.all()
}

def home(request):
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Contact'})
