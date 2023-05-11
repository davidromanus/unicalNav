from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	author=models.ForeignKey(User, on_delete=models.CASCADE)
	content=models.CharField(blank=0, max_length=280)
	date_posted=models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
	author=models.ForeignKey(User, on_delete=models.CASCADE)
	comment=models.CharField(blank=0, max_length=280)
	date_posted=models.DateTimeField(auto_now_add=True)
	ref_post=models.ForeignKey(Post, on_delete=models.CASCADE)
		

		
