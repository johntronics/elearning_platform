"""
URL configuration for elearning_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views

# API ViewSets
from users.api import UserViewSet, StatusUpdateViewSet
from courses.api import CourseViewSet

# Web Views
from users.views import dashboard
from chat.views import chat_room

# Create a router to register our API viewsets
router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'status', StatusUpdateViewSet)
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # apis
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    

    # frontend views
    path('', dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('chat/<int:user_id>/', chat_room, name='chat_room'),
    path('courses/', include('courses.urls')),
]