from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=300)
	slug = models.SlugField(max_length=300)
	body = RichTextUploadingField(blank=True, null=True)
	image = models.ImageField(upload_to='blog_images/')
	category = models.CharField(max_length=20)
	tags = models.CharField(max_length=30)
	date = models.DateField()

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-date"]


class Contact(models.Model):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	subject = models.CharField(max_length=100)
	body = models.TextField()
	date = models.DateField()

	def __str__(self):
		return self.subject

class NewsSubscriber(models.Model):
	email = models.CharField(max_length=100)

	def __str__(self):
		return self.email