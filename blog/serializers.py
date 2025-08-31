
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post

# Serializer for Post model
class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Show username instead of ID

    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'image', 'created_at']


# Optional: Serializer for User registration (if using API registration)
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
