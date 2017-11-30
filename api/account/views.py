from django.contrib.auth import get_user_model

from rest_framework import generics

from account import serializers


class RegistrationView(generics.CreateAPIView):
    """
    Register a new user.
    """
    model = get_user_model()
    serializer_class = serializers.RegistrationSerializer
