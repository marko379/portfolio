from django.db import models
from django.utils.text import slugify
# from io import BytesIO
from PIL import Image
from django.core.files import File
# from django.conf import settings
# from django.contrib.auth.models import User




class Projects(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	video = models.FileField(upload_to="videos",blank=True, null=True)
	image = models.ImageField(upload_to='project_images/',blank=True, null=True)
	slug = models.SlugField(blank=True, null=True)

	def __str__(self):
		return self.name


	def image_path(self):
		# return 'http://127.0.0.1:8000' + self.image.url
		return 'https://web-production-6895.up.railway.app' + self.image.url


	def video_path(self):
		return 'https://web-production-6895.up.railway.app' + self.video.url
		# return 'http://127.0.0.1:8000' + self.video.url

	def save(self):
		self.slug = slugify(self.name)
		super().save()



