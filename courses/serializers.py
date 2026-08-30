from rest_framework import serializers
from .models import Course, Enrollment, Material, Feedback

class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'teacher', 'title', 'description', 'created_at']