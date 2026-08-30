from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import StatusUpdate

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'is_student', 'is_teacher', 'photo', 'bio']

class StatusUpdateSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = StatusUpdate
        fields = ['id', 'user', 'content', 'created_at']