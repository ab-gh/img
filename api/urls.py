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
    path('', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]