from django.contrib import admin
from .models import BlogType, Blog

"""
用户名:jianzl
密码:j1234567
"""

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')

    def __str__(self):
        return self.type_name


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog_type', 'author', 'create_time', 'last_update_time')


