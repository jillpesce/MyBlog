from django.db import models

class Post(models.Model):
	id = models.IntegerField(max_length=200, primary_key=True)
	title = models.CharField(max_length=200)
	description = models.TextField()
	image = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	date = models.CharField(max_length=200)
