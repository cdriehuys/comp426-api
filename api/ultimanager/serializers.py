from rest_framework import serializers

from ultimanager import models


class GameSerializer(serializers.ModelSerializer):
    """
    Serializer for a game.
    """

    class Meta:
        fields = ('id', 'team', 'opponent', 'starting_position')
        model = models.Game
        read_only_fields = ('team',)


class PlayerSerializer(serializers.ModelSerializer):
    """
    Serializer for the `Player` model.
    """

    class Meta:
        fields = ('id', 'name', 'number', 'team')
        model = models.Player
        read_only_fields = ('team',)


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'game', 'players', 'starting_position', 'status')
        model = models.Point
        read_only_fields = ('game',)


class TeamSerializer(serializers.ModelSerializer):
    """
    Serializer for the `Team` model.
    """

    class Meta:
        fields = ('id', 'name', 'user', 'image')
        model = models.Team
        read_only_fields = ('user',)
