from django.shortcuts import render #type: ignore
from .models import Post

# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'summ/home.html', context)

def about(request):
    return render(request, 'summ/about.html', {'title': 'About'})