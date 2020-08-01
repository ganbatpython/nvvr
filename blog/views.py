from django.shortcuts import render
from django.http import HttpResponse
from . models import Post, Category


def index(request):
    category_list = Category.objects.all().order_by('name')
    context = {
        'categories': category_list
    }
    return render(request, 'index.html',context)

def post(request):    
    category_list = Category.objects.all().order_by('name')
    post_list = Post.objects.all()

    context = {
        'categories': category_list,
        'posts':post_list
    }
    return render(request, "post.html", context)


