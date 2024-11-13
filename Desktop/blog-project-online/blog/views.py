from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit  import CreateView,UpdateView
from .models import Post 


# Create your views here.

class PostListview(ListView):
    model = Post
    template_name = "Post_list.html"
    
class postDetaIlView(DetailView):
    model = Post
    template_name = "post-detail.html"
    
class postCreateview(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title","author","body"]
    
class postupdateview(UpdateView):
    model = Post
    template_name= "update.html"
    fields = ["title","body"] 