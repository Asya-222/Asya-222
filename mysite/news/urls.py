from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .models import Article
from . import views

urlpatterns = [
    url(r'^$', ListView.as_view(queryset = Article.objects.all().order_by("-date")[:20],template_name = "news/posts.html") ),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Article,template_name = 'news/post.html')),
    url(r'^firstform/', views.index, name="index")
]