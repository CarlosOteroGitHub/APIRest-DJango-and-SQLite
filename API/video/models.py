from django.db import models

# Create your models here.
class Video(models.Model):

	#Campos del Modelo.
	title = models.CharField(max_length=50)
	description = models.TextField()
	slug = models.SlugField(max_length=50)
	created_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title