from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
	"""Регистрирует нового пользователя."""
	if request.method != 'POST':
		# Выводит пустую форму регистраций.
		form = UserCreationForm()
	else:
		# Обработка заполненной формы.
		form = UserCreationForm(request.POST)

		if form.is_valid():
			new_user = form.save()
			# Выполнение входа и перенаправление на домашную страницу.
			login(request, new_user)
			return redirect('library_app:index')

	# Вывести пустую или недействительную форму.
	context = {'form': form}
	return render(request, 'registration/register.html', context)