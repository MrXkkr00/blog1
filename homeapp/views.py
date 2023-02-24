from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post


# Create your views here.
class BlogDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogListviews(ListView):
    model = Post
    template_name = 'home.html'


class BlogNewView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogEdit(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy("home")
