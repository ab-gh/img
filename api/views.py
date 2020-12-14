from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
import json


from .serializers import ImageSerializer, UserSerializer
from .models import User, Image

# Create your views here.

@csrf_exempt
def image(request, image_id):
    """
    Returns an image from a given image id
    """
    if request.method == "GET":
        try:
            image = Image.objects.get(pk=image_id)
            serializer = ImageSerializer(image)
        except Image.DoesNotExist:
            return JsonResponse({"error": "Image not found."}, status=404)
        else:
            return JsonResponse(serializer.data)
    else:
        return HttpResponseNotAllowed("")
