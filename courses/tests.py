from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Course

# Create your tests here.


User = get_user_model()

class CourseApplicationTests(TestCase):
    def setUp(self):
        # test teacher
        self.teacher = User.objects.create_user(
            username='teacher_test', 
            password='password123', 
            is_teacher=True
        )
        # test course
        self.course = Course.objects.create(
            teacher=self.teacher,
            title='Test Driven Development',
            description='Learning how to test Django.'
        )
        # The API Client
        self.client = APIClient()

    def test_course_creation_model(self):
        """Test that the Course model creates instances correctly"""
        self.assertEqual(self.course.title, 'Test Driven Development')
        self.assertEqual(self.course.teacher.username, 'teacher_test')
        self.assertEqual(str(self.course), 'Test Driven Development')

    def test_api_course_list_unauthenticated(self):
        """Test that unauthenticated users cannot view the API"""
        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_course_list_authenticated(self):
        """Test that authenticated users CAN view the API"""
        self.client.force_authenticate(user=self.teacher)
        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verify the course is in the JSON response
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Test Driven Development')