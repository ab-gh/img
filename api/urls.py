from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
from api import views

urlpatterns = [
    path('images/', views.ImageList.as_view()),
    path('images/<int:pk>', views.ImageDetail.as_view()),
    path('tags/', views.TagList.as_view()),
    path('tags/<int:pk>', views.TagDetail.as_view()),
    path('tags/<int:pk>/images', views.TagImages.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('users/<int:pk>/images', views.UserImages.as_view())
]