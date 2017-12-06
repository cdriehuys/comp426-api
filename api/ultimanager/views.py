from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ultimanager import models, permissions, serializers


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
