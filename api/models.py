from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """
    User model inherits AbstractUser
    """
    def __str__(self):
        return f"{self.username}"

class Image(models.Model):
    """
    An image
    """
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=280)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="images")
    image = models.BinaryField(blank=True)

    def __str__(self):
        return f"{self.title}"
    
    
