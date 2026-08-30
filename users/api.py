from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .models import StatusUpdate
from .serializers import UserSerializer, StatusUpdateSerializer

User = get_user_model()

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for users to be viewed.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class StatusUpdateViewSet(viewsets.ModelViewSet):
    queryset = StatusUpdate.objects.all().order_by('-created_at')
    serializer_class = StatusUpdateSerializer

    # Automatically make user to be the person making the request
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)