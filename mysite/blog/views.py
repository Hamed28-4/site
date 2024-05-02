from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import AccountForm


async def method_name():
    pass

def home(request):
    return HttpResponse("Home Page")


def postlist(request):
    post = Post.objects.all()
    paginator = Paginator(post, 3)
    page = request.GET.get("page")
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    context = {"post": post, 'page': page}
    return render(request, 'post_list.html', context)


def postdetail(request, postid):
    post = Post.objects.get(id=postid)
    context = {"post": post}
    return render(request, 'post_details.html', context)


def users(request):
    if request.method == "POST":
        form = AccountForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AccountForm()
    return render(request, 'account.html', {"form": form})