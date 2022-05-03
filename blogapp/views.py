from dataclasses import fields
from pyexpat import model
from re import template
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.contrib.auth.models import User
from blogapp.models import Post
# Create your views here.

# view with function
def main(request):
    # posts = Post.objects.filter(Post.author)      add {'posts' : posts})
    return render(request, 'main_page.html', {})

# Class view
class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model=Post
    template_name = 'add_post.html'
    fields = '__all__'

 