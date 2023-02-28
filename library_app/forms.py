from django import forms
from .models import (
	AddBook,
	AddSong,
	AddPhoto,
	AddVideo
)


class AddBookForm(forms.ModelForm):
	"""Форма для добавления книг."""
	class Meta:
		model = AddBook
		fields = ['title', 'author', 'book']
		labels = {'title': 'Название', 'author': 'Автор', 'book': 'Книга'}


class AddSongForm(forms.ModelForm):
	"""Форма для добавления песен."""
	class Meta:
		model = AddSong
		fields = ['title', 'author', 'song']
		labels = {'title': 'Название', 'author': 'Автор', 'song': 'Песня'}


class AddPhotoForm(forms.ModelForm):
	"""Форма для добавления фото."""
	class Meta:
		model = AddPhoto
		fields = ['title', 'photo']
		labels = {'title': 'Название', 'photo': 'Фото'}


class AddVideoForm(forms.ModelForm):
	"""Форма для добавления фотографий."""
	class Meta:
		model = AddVideo
		fields = ['title', 'video']
		labels = {'title': 'Название', 'video': 'Видео'}