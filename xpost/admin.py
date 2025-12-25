from django.contrib import admin

from xpost.models import Post


@admin.register (Post)
class PostAdmin (admin.ModelAdmin):
    list_display = [
        "title",
        "file",
    ]

