from rest_framework import generics, permissions  # add permissions import
from .serializers import UserSerializer
from django.contrib.auth.models import User

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # <-- allow anyone to register
