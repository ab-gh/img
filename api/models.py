from django.db import models
from django.contrib.auth.models import AbstractUser
import base64

# Create your models here.

class User(AbstractUser):
    """
    User model inherits AbstractUser
    """
    def __str__(self):
        return f"{self.username}"

class Tag(models.Model):
    """
    A tag, which images can have multiple of
    """
    name = models.CharField(max_length=40, unique=True)
    
    def __str__(self):
        return f"{self.name}"
    

class Image(models.Model):
    """
    An image
    """
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=280)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="images")
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.TextField(blank=False)
    mime = models.CharField(max_length=127, blank=True)
    tags = models.ManyToManyField(Tag, related_name="images", blank=False)

    class Meta:
        ordering = ['-timestamp',]

    def __str__(self):
        return f"{self.title}"


    
