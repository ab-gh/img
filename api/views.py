from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def image(request, image_id):
    return(HttpResponse(image_id))