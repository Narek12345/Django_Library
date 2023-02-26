from django.db import models
from django.contrib.auth.models import User


class AddBook(models.Model):
	"""Модель для добавления книг."""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=150)
	author = models.CharField(max_length=50, blank=True)
	book = models.FileField(upload_to="books/%Y/%m/%d/")
	publication_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Возвращает строковое представление модели."""
		return self.title


class AddSong(models.Model):
	"""Модель для добавления песен."""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=50, blank=True)
	song = models.FileField(upload_to="songs/%Y/%m/%d/")
	publication_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Возвращает строковое представление модели."""
		return self.title


class AddPhoto(models.Model):
	"""Модель для добавления фотографий."""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=150)
	photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
	publication_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Возвращает строковое представление модели."""
		return self.title


class AddVideo(models.Model):
	"""Модель для добавления фотографий."""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=150)
	video = models.FileField(upload_to="videos/%Y/%m/%d/")
	publication_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Возвращает строковое представление модели."""
		return self.title