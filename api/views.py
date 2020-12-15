from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json

from django_filters.rest_framework.filterset import FilterSet
import coreapi

from .serializers import ImageSerializer, UserSerializer
from .models import User, Image

# Create your views here.

class ImageFilter(FilterSet):

    class Meta(object):
        models = Image
        fields = (
            'id', 'title', 'content', 'user', 'timestamp', 'image', 'mime',)

class ImageList(generics.ListCreateAPIView):
    """
    Lists all images
    """
    model = Image
    serializer_class = ImageSerializer
    filter_class = ImageFilter

    def get(self, request, format=None):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)

class ImageDetail(generics.RetrieveAPIView):
    """
    Retrieve an image
    """
    model = Image
    serializer_class = ImageSerializer
    filter_class = ImageFilter
    
    def get_image(self, pk):
        try:
            return Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        image = self.get_image(pk)
        serializer = ImageSerializer(image)
        return Response(serializer.data)

    
