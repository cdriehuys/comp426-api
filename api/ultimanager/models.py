"""
Models for representing each type of object in the database.
"""

from django.conf import settings
from django.db import models


class Team(models.Model):
    """
    A team is a collection of players managed by a user. A team can play
    in multiple games.
    """
    image = models.ImageField(
        blank=True,
        help_text="The team's logo.",
        null=True,
        upload_to='images/teams/')
    name = models.CharField(
        help_text="The team's name.",
        max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        help_text="The user who manages the team.",
        on_delete=models.CASCADE,
        related_name='teams',
        related_query_name='team')

    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'teams'

    def __str__(self):
        """
        Get a string representation of the team.
        """
        return self.name
