from django.contrib import admin
from apps.library import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    ...
