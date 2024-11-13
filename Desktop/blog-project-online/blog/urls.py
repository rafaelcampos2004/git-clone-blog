from django.urls import path
from .views import PostListview,postDetaIlView,postCreateview

urlpatterns = [
    path("",PostListview.as_view(), name="home"),
    path("post/<int:pk>/", postDetaIlView.as_view(), name="post_detail"),
    path("post/new/",postCreateview.as_view(), name="post_new"),
]
