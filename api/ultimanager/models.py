"""
Models for representing each type of object in the database.
"""

from django.conf import settings
from django.db import models


class GamePosition:
    """
    Holds constants for referencing game positions.
    """
    DEFENSE = 'D'
    OFFENSE = 'O'

    CHOICES = (
        (DEFENSE, 'Defense'),
        (OFFENSE, 'Offense'),
    )


class Game(models.Model):
    """
    A game contains all the information about a match against an
    opposing team.
    """
    opponent = models.CharField(
        help_text="The name of the opposing team.",
        max_length=255)
    starting_position = models.CharField(
        choices=GamePosition.CHOICES,
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

    @property
    def home_points(self):
        return self.points.filter(status=Point.HOME_SCORED).count()

    @property
    def opponent_points(self):
        return self.points.filter(status=Point.OPPONENT_SCORED).count()


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

    @property
    def num_completions(self):
        return Throw.objects.exclude(
            result=Throw.TURNOVER).filter(
            thrower=self).count()

    @property
    def num_throws(self):
        return Throw.objects.filter(thrower=self).count()

    @property
    def num_turns(self):
        return Throw.objects.filter(
            thrower=self,
            result=Throw.TURNOVER).count()

    @property
    def num_points(self):
        return Point.objects.filter(players=self).count()

    @property
    def num_games(self):
        return Game.objects.filter(
            point__players=self).count()

    @property
    def avg_completions_per_point(self):
        if self.num_points == 0:
            return 0

        return self.num_completions / self.num_points

    @property
    def avg_points_per_game(self):
        if self.num_games == 0:
            return 0

        return self.num_points / self.num_games

    @property
    def completion_percentage(self):
        if self.num_throws == 0:
            return 0

        return self.num_completions / self.num_throws


class Point(models.Model):
    """
    A single point of a game.
    """
    IN_PROGRESS = 'P'
    HOME_SCORED = 'H'
    OPPONENT_SCORED = 'O'

    STATUS_CHOICES = (
        (IN_PROGRESS, 'In Progress'),
        (HOME_SCORED, 'Home Team Scored'),
        (OPPONENT_SCORED, 'Opposing Team Scored'),
    )

    # Fields
    game = models.ForeignKey(
        'ultimanager.Game',
        help_text="The game that the point is a part of.",
        on_delete=models.CASCADE,
        related_name='points',
        related_query_name='point')
    players = models.ManyToManyField(
        'ultimanager.Player',
        help_text="The players that played the point.",
        related_name='points',
        related_query_name='point')
    starting_position = models.CharField(
        choices=GamePosition.CHOICES,
        help_text="The position that the home team is starting the point on.",
        max_length=1)
    status = models.CharField(
        choices=STATUS_CHOICES,
        help_text=("The state that the point is in. If the point is complete, "
                   "this field tracks which team scored."),
        max_length=1)

    class Meta:
        verbose_name = 'point'
        verbose_name_plural = 'points'

    def __str__(self):
        """
        Get a string representation of the instance.
        """
        return "Point in {home} vs. {away}".format(
            away=self.game.opponent,
            home=self.game.team.name)


class Possession(models.Model):
    """
    A sequence of throws.
    """
    REASON_D = 'D'
    REASON_PULL = 'P'
    REASON_TURNOVER = 'T'

    REASON_CHOICES = (
        (REASON_D, 'Got a D'),
        (REASON_PULL, 'Pulled to'),
        (REASON_TURNOVER, 'Turnover')
    )

    # Fields
    defensive_player = models.ForeignKey(
        'ultimanager.Player',
        blank=True,
        help_text="The player who go the D to start the possession.",
        null=True,
        on_delete=models.SET_NULL,
        related_name='defensive_possessions',
        related_query_name='defensive_possession')
    point = models.ForeignKey(
        'ultimanager.Point',
        help_text="The point the possession is a part of.",
        on_delete=models.CASCADE,
        related_name='possessions',
        related_query_name='possession')
    reason = models.CharField(
        choices=REASON_CHOICES,
        help_text="The reason the possession was started.",
        max_length=1)

    class Meta:
        verbose_name = 'possession'
        verbose_name_plural = 'possessions'

    def __str__(self):
        """
        Get a string representation of the instance.
        """
        return "Possession in {point}".format(point=self.point)


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

    @property
    def games_lost(self):
        lost = 0
        for game in Game.objects.filter(team=self):
            points_won = game.points.filter(status=Point.HOME_SCORED).count()
            points_lost = game.points.filter(
                status=Point.OPPONENT_SCORED).count()

            if points_won < points_lost:
                lost += 1

        return lost

    @property
    def games_won(self):
        won = 0
        for game in Game.objects.filter(team=self):
            points_won = game.points.filter(status=Point.HOME_SCORED).count()
            points_lost = game.points.filter(
                status=Point.OPPONENT_SCORED).count()

            if points_won > points_lost:
                won += 1

        return won

    @property
    def num_games(self):
        return self.games.count()


class Throw(models.Model):
    """
    A throw from one player to another.
    """
    # Throw type constants
    BACKHAND = 'B'
    FOREHAND = 'F'
    OTHER = 'O'

    TYPE_CHOICES = (
        (BACKHAND, 'Backhand'),
        (FOREHAND, 'Forehand'),
        (OTHER, 'Other'),
    )

    # Throw result constants
    COMPLETION = 'C'
    GOAL = 'G'
    TURNOVER = 'T'

    RESULT_CHOICES = (
        (COMPLETION, 'Completion'),
        (GOAL, 'Goal'),
        (TURNOVER, 'Turnover')
    )

    # Fields
    possession = models.ForeignKey(
        'ultimanager.Possession',
        help_text="The possession the throw is a part of.",
        on_delete=models.CASCADE,
        related_name='throws',
        related_query_name='throw')
    receiver = models.ForeignKey(
        'ultimanager.Player',
        help_text="The player who received the pass.",
        null=True,
        on_delete=models.SET_NULL,
        related_name='received_throws',
        related_query_name='received_throw')
    result = models.CharField(
        choices=RESULT_CHOICES,
        help_text="The result of the throw.",
        max_length=1)
    throw_type = models.CharField(
        choices=TYPE_CHOICES,
        help_text="The type of the throw.",
        max_length=1)
    thrower = models.ForeignKey(
        'ultimanager.Player',
        help_text="The player who threw the pass.",
        null=True,
        on_delete=models.SET_NULL,
        related_name='throws',
        related_query_name='throw')

    class Meta:
        verbose_name = 'throw'
        verbose_name_plural = 'throws'

    def __str__(self):
        """
        Get a string representation of the instance.
        """
        return '{thrower} to {receiver} ({throw_type})'.format(
            receiver=self.receiver,
            throw_type=self.get_throw_type_display(),
            thrower=self.thrower)
