from django.urls import path
from .views import PostListview,postDetaIlView,postCreateview,postupdateview

urlpatterns = [
    path("",PostListview.as_view(), name="home"),
    path("post/<int:pk>/", postDetaIlView.as_view(), name="post_detail"),
    path("post/new/",postCreateview.as_view(), name="post_new"),
    path("post/<int:pk>/edit/", postupdateview.as_view(), name="update"),
]
