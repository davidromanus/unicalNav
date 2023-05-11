from django.urls import path
from .views import PostListView,CreatePostView
from . import views


urlpatterns=[
	path('', views.index, name="index"),
	path('main/', PostListView.as_view(), name="main"),
	path('main/new', CreatePostView.as_view(), name="create-post")
]