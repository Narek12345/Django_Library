from django.contrib import admin
from .models import AddBook, AddSong, AddPhoto, AddVideo


# Добавление модели AddBook.
admin.site.register(AddBook)

# Добавление модели AddSong.
admin.site.register(AddSong)

# Добавление модели AddPhoto.
admin.site.register(AddPhoto)

# Добавления модели AddVideo.
admin.site.register(AddVideo)