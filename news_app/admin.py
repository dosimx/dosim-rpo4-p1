from django.contrib import admin

# Register your models here.
from .models import Category, Post, Adv

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Adv)