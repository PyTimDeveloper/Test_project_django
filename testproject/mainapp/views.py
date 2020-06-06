from django.shortcuts import render 
from .models import Post



def index(request):
    post = Post.objects.all()
    context = {
        'post': post,
    }
    return render(request, 'mainapp/index.html', context)