from django.contrib import admin
from .models import Post

# Register your models here.

class PostConfig(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Post, PostConfig)