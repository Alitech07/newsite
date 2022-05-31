from unicodedata import category
from django.contrib import admin
from .models.articles import Post,Category

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
