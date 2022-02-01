from django.contrib import admin

from .models import Board, Folder, TodoItem, Tags, User

# Register your models here.
models = [Board, Folder, TodoItem, Tags, User]
for model in models:
    admin.site.register(model)
