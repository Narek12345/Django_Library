"""URL schemes for the "library_app" app."""

from . import views
from django.urls import path


app_name = "library_app"
urlpatterns = [
	# Домашняя страница.
	path('', views.index, name="index"),
	# Страница для добавления книг.
	path('new_book/', views.new_book, name="new_book"),
	# Страница для добавления песен.
	path('new_song/', views.new_song, name="new_song"),
	# Страница для добавления фото.
	path('new_photo/', views.new_photo, name="new_photo"),
	# Страница для добавления видео.
	path('new_video/', views.new_video, name="new_video"),
	# Страница для просмотра всех книг.
	path('view_all_books/', views.view_all_books, name="view_all_books"),
	# Страница для просмотра всех песен.
	path('view_all_songs/', views.view_all_songs, name="view_all_songs"),
	# Страница для просмотра всех фото.
	path('view_all_photos', views.view_all_photos, name="view_all_photos"),
	# Страница для просмотра всех видео.
	path('view_all_videos/', views.view_all_videos, name="view_all_videos"),
	# Страница для просмотра конкретной книги.
	path('view_book/<int:book_id>', views.view_book, name="view_book"),
	# Страница для просмотра конкретной песни.
	path('view_song/<int:song_id>', views.view_song, name="view_song"),
	# Страница для просмотра конкретного фото.
	path('view_photo/<int:photo_id>', views.view_photo, name="view_photo"),
	# Страница для просмотра конкретного видео.
	path('view_video/<int:video_id>', views.view_video, name="view_video"),
]