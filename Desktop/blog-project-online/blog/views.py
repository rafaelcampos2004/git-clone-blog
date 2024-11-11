from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post
# Create your views here.

class PostListview(ListView):
    model = Post
    template_name = "Post_list.html"
    
class postDetaIlView(DetailView):
    model = Post
    template_name = "post-detail.html"