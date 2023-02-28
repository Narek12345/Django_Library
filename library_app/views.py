from django.shortcuts import render, redirect
from datetime import datetime
from .forms import (
	AddBookForm,
	AddSongForm,
	AddPhotoForm,
	AddVideoForm
)


def index(request):
	"""Домашняя страница."""
	return render(request, 'library_app/index.html')


def new_book(request):
	"""Добавляет новую книгу."""
	if request.method != 'POST':
		# Данные не отправлялись; создается пустая форма.
		form = AddBookForm()
	else:
		# Отправлены данные POST; обработать данные.
		form = AddBookForm(request.POST, request.FILES)
		if form.is_valid():
			new_book = form.save(commit=False)
			new_book.user = request.user
			new_book.save()
			return redirect('library_app:index')

	# Вывести пустую или недействительную форму.
	context = {'form': form}
	return render(request, 'library_app/new_book.html', context)


def new_song(request):
	"""Добавляет новую песню."""
	if request.method != 'POST':
		# Данные не отправлялись; создается пустая форма.
		form = AddSongForm()
	else:
		# Отправлены данные POST; обработать данные.
		form = AddSongForm(request.POST, request.FILES)
		if form.is_valid():
			new_song = form.save(commit=False)
			new_song.user = request.user
			new_song.save()
			return redirect('library_app:index')

	# Вывести пустую или недеqствительную форму.
	context = {'form': form}
	return render(request, 'library_app/new_song.html', context)


def new_photo(request):
	"""Добавляет новое фото."""
	if request.method != 'POST':
		# Данные не отправлялись; создается пустая форма.
		form = AddPhotoForm()
	else:
		# Отправлены данные POST; обработать данные.
		form = AddPhotoForm(request.POST, request.FILES)
		if form.is_valid():
			new_photo = form.save(commit=False)
			new_photo.user = request.user
			new_photo.save()
			return redirect('library_app:index')

	# Вывести пустую или недействительную форму.
	context = {'form': form}
	return render(request, 'library_app/new_photo.html', context)


def new_video(request):
	"""Добавляет новое видео."""
	if request.method != 'POST':
		# Данные не отправлялись; создается пустая форма.
		form = AddVideoForm()
	else:
		# Отправлены данные POST; обработать данные.
		form = AddVideoForm(request.POST, request.FILES)
		if form.is_valid():
			new_video = form.save(commit=False)
			new_video.user = request.user
			new_video.save()
			return redirect('library_app:index')

	# Вывести пустую или недействительную форму.
	context = {'form': form}
	return render(request, 'library_app/new_video.html', context)