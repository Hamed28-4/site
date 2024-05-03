from django.contrib import admin
from .models import Post, Account

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time')
    list_filter = ('date',)