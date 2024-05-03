from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("postlist/", views.postlist, name="postlist"),
    path("postlist/postdetail/<postid>", views.postdetail, name="postdetail")
    ]