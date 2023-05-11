from django.shortcuts import render
from django.views.generic import ListView,CreateView
from . models import Post


def index(request):
	return render(request,"main/index.html")

	
class PostListView(ListView):
	model= Post
	template_name='main/main.html'
	context_object_name='posts'
	ordering = ['-date_posted']

class CreatePostView(CreateView):
	model=Post
	fields = ['content']
		
		