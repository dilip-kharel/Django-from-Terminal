from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from secApp.models import Post
from . import views

urlpatterns = [
    url(r'^jam/', views.jam, name='jam'),
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("date")[:25], template_name="secApp/blog.html")), url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post, template_name = 'secApp/post.html')),
    
]