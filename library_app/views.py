from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404
from datetime import datetime

from .models import (
	AddBook,
	AddSong,
	AddPhoto,
	AddVideo
)
from .forms import (
	AddBookForm,
	AddSongForm,
	AddPhotoForm,
	AddVideoForm
)


def index(request):
	"""Домашняя страница."""
	return render(request, 'library_app/index.html')

@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
def view_all_books(request):
	"""Просмотр добавленных книг."""
	# Берем из БД все добавленные книги.
	all_books = AddBook.objects.all()[::-1]
	db_info = None
	error_info = None

	# Проверяем не пусто ли наше БД.
	if len(all_books) != 0:
		db_info = all_books
	else:
		error_info = "Вы еще не добавили данные в БД."

	context = {'db_info': db_info, 'error_info': error_info}
	return render(request, 'library_app/view_all_books.html', context)


@login_required
def view_all_songs(request):
	"""Просмотр добавленных песен."""
	# Берем из БД все добавленные книги.
	all_songs = AddSong.objects.all()[::-1]
	db_info = None
	error_info = None

	# Проверяем не пусто ли наше БД.
	if len(all_songs) != 0:
		db_info = all_songs
	else:
		error_info = "Вы еще не добавили данные в БД."

	context = {'db_info': db_info, 'error_info': error_info}
	return render(request, 'library_app/view_all_songs.html', context)


@login_required
def view_all_photos(request):
	"""Просмотр добавленных песен."""
	# Берем из БД все добавленные книги.
	all_photos = AddPhoto.objects.all()[::-1]
	db_info = None
	error_info = None

	# Проверяем не пусто ли наше БД.
	if len(all_photos) != 0:
		db_info = all_photos
	else:
		error_info = "Вы еще не добавили данные в БД."

	context = {'db_info': db_info, 'error_info': error_info}
	return render(request, 'library_app/view_all_photos.html', context)


@login_required
def view_all_videos(request):
	"""Просмотр добавленных песен."""
	# Берем из БД все добавленные книги.
	all_videos = AddVideo.objects.all()[::-1]
	db_info = None
	error_info = None

	# Проверяем не пусто ли наше БД.
	if len(all_videos) != 0:
		db_info = all_videos
	else:
		error_info = "Вы еще не добавили данные в БД."

	context = {'db_info': db_info, 'error_info': error_info}
	return render(request, 'library_app/view_all_videos.html', context)


@login_required
def view_book(request, book_id):
	"""Просмотр конкретной книги."""
	book = AddBook.objects.get(id=book_id)
	return render(request, 'library_app/view_book.html', {'book': book})


@login_required
def view_song(request, song_id):
	"""Просмотр конкретной песни."""
	song = AddSong.objects.get(id=song_id)
	return render(request, 'library_app/view_song.html', {'song': song})


@login_required
def view_photo(request, photo_id):
	"""Просмотр конкретной книги."""
	photo = AddPhoto.objects.get(id=photo_id)
	return render(request, 'library_app/view_photo.html', {'photo': photo})


@login_required
def view_video(request, video_id):
	"""Просмотр конкретного видео."""
	video = AddVideo.objects.get(id=video_id)
	return render(request, 'library_app/view_video.html', {'video': video})