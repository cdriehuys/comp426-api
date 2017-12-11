"""
Models for representing each type of object in the database.
"""

from django.conf import settings
from django.db import models


class Game(models.Model):
    """
    A game contains all the information about a match against an
    opposing team.
    """
    # Game position constants
    DEFENSE = 'O'
    OFFENSE = 'D'

    POSITION_CHOICES = (
        (DEFENSE, 'Defense'),
        (OFFENSE, 'Offense'),
    )

    # Fields
    opponent = models.CharField(
        help_text="The name of the opposing team.",
        max_length=255)
    starting_position = models.CharField(
        choices=POSITION_CHOICES,
        help_text="The position that the home team started the game on.",
        max_length=1)
    team = models.ForeignKey(
        'ultimanager.Team',
        help_text="The team being tracked in the game.",
        on_delete=models.CASCADE,
        related_name='games',
        related_query_name='game')

    def __str__(self):
        """
        Get a string representation of the instance.
        """
        return "{home} vs. {away}".format(
            away=self.opponent,
            home=self.team.name)


class Player(models.Model):
    """
    A player is a member of a team.
    """
    name = models.CharField(
        help_text="The player's name.",
        max_length=255)
    number = models.PositiveSmallIntegerField(
        help_text="The player's number.")
    team = models.ForeignKey(
        'ultimanager.Team',
        help_text="The team that the player belongs to.",
        on_delete=models.CASCADE,
        related_name='players',
        related_query_name='player')

    class Meta:
        verbose_name = 'player'
        verbose_name_plural = 'players'

    def __str__(self):
        """
        Get a string representation of the player.
        """
        return self.name


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
