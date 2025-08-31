from django.contrib import admin
from .models import Post

admin.site.register(Post)

from django.contrib import admin
from .models import Post, Category, Comment

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
