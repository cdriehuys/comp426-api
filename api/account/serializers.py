from django.contrib.auth import get_user_model, password_validation

from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for a user's profile.
    """

    class Meta:
        extra_kwargs = {
            'username': {
                'help_text': "The user's username.",
            },
        }
        fields = ('id', 'username')
        model = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for registering a new user.
    """

    class Meta:
        extra_kwargs = {
            'password': {
                'help_text': "The user's password.",
                'style': {'input_type': 'password'},
                'write_only': True,
            },
            'username': {
                'help_text': "The user's username.",
            },
        }
        fields = ('username', 'password')
        model = get_user_model()

    def save(self):
        """
        Register the user.
        """
        get_user_model().objects.create_user(**self.validated_data)

    def validate_password(self, password):
        """
        Validate the password that the user gave.
        """
        # This will raise a ValidationError if it fails.
        password_validation.validate_password(password)

        return password
