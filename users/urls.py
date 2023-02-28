"""URL schemes for the "users" app."""

from django.urls import path, include
from . import views


app_name = "users"
urlpatterns = [
	# Включить URL авторизаций по умолчанию.
	path('', include('django.contrib.auth.urls')),
	# Страница регистраций.
	path('register/', views.register, name="register"),
]