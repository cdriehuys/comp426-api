from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ultimanager import models, permissions, serializers


class GameDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        permissions.IsGameManagerOrReadOnly)
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer


class GameListView(generics.ListCreateAPIView):
    """
    create:
    Create a new game.

    list:
    List the games tracked by the team whose ID is given in the URL.
    """
    filter_backends = (OrderingFilter,)
    ordering = ('opponent',)
    ordering_fields = ('opponent',)
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        permissions.IsGameManagerOrReadOnly)
    serializer_class = serializers.GameSerializer

    def get_queryset(self):
        team = get_object_or_404(models.Team, pk=self.kwargs.get('pk'))

        return team.games.all()

    def perform_create(self, serializer):
        team = get_object_or_404(models.Team, pk=self.kwargs.get('pk'))

        return serializer.save(team=team)


class PlayerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    destroy:
    Delete the player with the specified ID.

    partial_update:
    Partially update a specific player's information.

    retrieve:
    Retrieve the details of a specific player.

    update:
    Update a specific player's information.
    """
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        permissions.IsPlayerManagerOrReadOnly)
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer


class PlayerListView(generics.ListCreateAPIView):
    """
    create:
    Create a new player.

    The player will be assigned to the team whose ID is given in the
    URL.

    list:
    List the players on the team whose ID is given in the URL.
    """
    filter_backends = (OrderingFilter,)
    ordering = ('name',)
    ordering_fields = ('name', 'number')
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        permissions.IsPlayerManagerOrReadOnly)
    serializer_class = serializers.PlayerSerializer

    def get_queryset(self):
        """
        Return the players who belong to the team whose ID is given in
        the URL of the request.
        """
        team = get_object_or_404(models.Team, pk=self.kwargs.get('pk'))

        return team.players.all()

    def perform_create(self, serializer):
        """
        Associate the newly created player with the current team.
        """
        team = get_object_or_404(models.Team, pk=self.kwargs.get('pk'))

        return serializer.save(team=team)


class PointDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        permissions.IsPointManagerOrReadOnly)
    queryset = models.Point.objects.all()
    serializer_class = serializers.PointSerializer


class PointListView(generics.ListCreateAPIView):
    filter_backends = (OrderingFilter,)
    ordering = ('id',)
    ordering_fields = ('id',)
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        permissions.IsPointManagerOrReadOnly)
    serializer_class = serializers.PointSerializer

    def get_queryset(self):
        game = get_object_or_404(models.Game, pk=self.kwargs.get('pk'))

        return game.points.all()

    def perform_create(self, serializer):
        game = get_object_or_404(models.Game, pk=self.kwargs.get('pk'))

        return serializer.save(game=game)


class PossessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        permissions.IsPossessionManagerOrReadOnly)
    queryset = models.Possession.objects.all()
    serializer_class = serializers.PossessionSerializer


class PossessionListView(generics.ListCreateAPIView):
    filter_backends = (OrderingFilter,)
    ordering = ('id',)
    ordering_fields = ('id',)
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        permissions.IsPossessionManagerOrReadOnly)
    serializer_class = serializers.PossessionSerializer

    def get_queryset(self):
        point = get_object_or_404(models.Point, pk=self.kwargs.get('pk'))

        return point.possessions.all()

    def perform_create(self, serializer):
        point = get_object_or_404(models.Point, pk=self.kwargs.get('pk'))

        return serializer.save(point=point)


class TeamViewSet(viewsets.ModelViewSet):
    """
    Collection of views for managing a list of teams.

    create:
    Create a new team managed by the current user.

    delete:
    Delete a specific team.

    This action can only be performed by the user who owns the team.

    list:
    List all the teams tracked by the API.

    partial_update:
    Partially update a team's information.

    read:
    Retrieve the details of a specific team.

    update:
    Update a team's information.
    """
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('user',)
    ordering_fields = ('name', 'user')
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        permissions.IsOwnerOrReadOnly)
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer

    def perform_create(self, serializer):
        """
        Include the requesting user when creating a new team.
        """
        return serializer.save(user=self.request.user)
