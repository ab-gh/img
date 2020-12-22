from django.contrib import admin

from .models import User, Image, Tag

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "user", "image")

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'images')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')


admin.site.register(User, UserAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Tag, TagAdmin)