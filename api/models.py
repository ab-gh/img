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

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username
        }

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

    class Meta:
        ordering = ['-timestamp',]

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "image": self.image,
            "mime": self.mime,
            "user": self.user.serialize()
        }

    def __str__(self):
        return f"{self.title}"
    
    
