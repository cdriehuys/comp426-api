from rest_framework import serializers

from ultimanager import models


class TeamSerializer(serializers.ModelSerializer):
    """
    Serializer for the `Team` model.
    """

    class Meta:
        fields = ('id', 'name', 'user', 'image')
        model = models.Team
        read_only_fields = ('user',)
