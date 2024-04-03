from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    return HttpResponse("Home Page")


def postlist(request):
    post = Post.objects.all()
    context = {"post": post}
    return render(request, 'post_list.html', context)


def postdetail(request, postid):
    post = Post.objects.get(id=postid)
    context = {"post": post}
    return render(request, 'post_details.html', context)