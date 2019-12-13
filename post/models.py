from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	image = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	date = models.CharField(max_length=200)


	def __str__(self):
		return self.title