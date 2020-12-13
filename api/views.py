from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed

# Create your views here.

def image(request, image_id):
    """
    Returns an image from a given image id
    """
    if request.method == "GET":
        HttpResponse(image_id)
    else:
        return HttpResponseNotAllowed("Method not allowed")
