from rest_framework import serializers

from ultimanager import models


class GameSerializer(serializers.ModelSerializer):
    """
    Serializer for a game.
    """

    class Meta:
        fields = (
            'id', 'team', 'opponent', 'starting_position', 'home_points',
            'opponent_points'
        )
        model = models.Game
        read_only_fields = ('team',)


class PlayerSerializer(serializers.ModelSerializer):
    """
    Serializer for the `Player` model.
    """
    class Meta:
        fields = (
            'id', 'name', 'number', 'team', 'num_throws', 'num_completions',
            'completion_percentage', 'num_turns', 'num_points', 'num_games',
            'avg_completions_per_point', 'avg_points_per_game'
        )
        model = models.Player
        read_only_fields = ('team',)


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'game', 'players', 'starting_position', 'status')
        model = models.Point
        read_only_fields = ('game',)


class PossessionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'point', 'reason', 'defensive_player')
        model = models.Possession
        read_only_fields = ('point',)


class TeamSerializer(serializers.ModelSerializer):
    """
    Serializer for the `Team` model.
    """

    class Meta:
        fields = (
            'id', 'name', 'user', 'image', 'games_lost', 'games_won',
            'num_games'
        )
        model = models.Team
        read_only_fields = ('user',)


class ThrowSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id', 'possession', 'thrower', 'receiver', 'throw_type', 'result'
        )
        model = models.Throw
        read_only_fields = ('possession',)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.instance.result == models.Throw.GOAL:
            self.instance.possession.point.status = models.Point.HOME_SCORED
            self.instance.possession.point.save()
