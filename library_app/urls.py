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
]