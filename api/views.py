from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
        except Image.DoesNotExist:
            return JsonResponse({"error": "Image not found."}, status=404)
        else:
            return JsonResponse(image.serialize())
    else:
        return HttpResponseNotAllowed("")
