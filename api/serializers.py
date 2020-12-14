from rest_framework import serializers
from .models import Image, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ImageSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Image
        fields = ['id', 'title', 'content', 'user', 'timestamp', 'image', 'mime']

