from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from account import serializers


class ProfileView(generics.RetrieveAPIView):
    """
    Retrieve the current user's profile.
    """
    model = get_user_model
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProfileSerializer

    def get_object(self):
        """
        Get the requesting user.
        """
        return self.request.user


class RegistrationView(generics.CreateAPIView):
    """
    Register a new user.
    """
    model = get_user_model()
    serializer_class = serializers.RegistrationSerializer
