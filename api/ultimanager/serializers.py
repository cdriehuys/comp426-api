from rest_framework import serializers

from ultimanager import models


class PlayerSerializer(serializers.ModelSerializer):
    """
    Serializer for the `Player` model.
    """

    class Meta:
        fields = ('id', 'name', 'number', 'team')
        model = models.Player
        read_only_fields = ('team',)


class TeamSerializer(serializers.ModelSerializer):
    """
    Serializer for the `Team` model.
    """

    class Meta:
        fields = ('id', 'name', 'user', 'image')
        model = models.Team
        read_only_fields = ('user',)
