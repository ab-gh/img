from django.contrib import admin

from .models import User, Image

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "user", "image")


admin.site.register(User)
admin.site.register(Image, ImageAdmin)