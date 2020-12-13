from django.urls import path

from . import views

urlpatterns = [
    path("image/<int:image_id>", views.image, name="image")
]