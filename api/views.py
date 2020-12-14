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
import json


from .serializers import ImageSerializer, UserSerializer
from .models import User, Image

# Create your views here.

class ImageList(APIView):
    """
    Lists all images
    """
    def get(self, request, format=None):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

class ImageDetail(APIView):
    """
    Retrieve an image
    """
    def get_image(self, pk):
        try:
            return Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        image = self.get_image(pk)
        serializer = ImageSerializer(image)
        return Response(serializer.data)

# @csrf_exempt
# def image(request, image_id):
#     """
#     Returns an image from a given image id
#     """
#     if request.method == "GET":
#         try:
#             image = Image.objects.get(pk=image_id)
#             serializer = ImageSerializer(image)
#         except Image.DoesNotExist:
#             return JsonResponse({"error": "Image not found."}, status=404)
#         else:
#             return JsonResponse(serializer.data)
#     else:
#         return HttpResponseNotAllowed("")

    
