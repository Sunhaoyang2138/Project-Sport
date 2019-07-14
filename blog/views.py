from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def homepage(request):
    return render(request, 'blog/homepage.html', {})