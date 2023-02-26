"""URL schemes for the "library_app" app."""

from . import views
from django.urls import path


app_name = "library_app"
urlpatterns = [
	# Домашняя страница.
	path('', views.index, name="index"),
]