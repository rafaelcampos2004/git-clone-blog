from django.urls import path
from .views import PostListview,postDetaIlView

urlpatterns = [
    path("",PostListview.as_view(), name="home"),
    path("post/<int:pk>/", postDetaIlView.as_view(), name="post_detail"),
]
