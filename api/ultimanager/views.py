from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ultimanager import models, permissions, serializers


class TeamViewSet(viewsets.ModelViewSet):
    """
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
