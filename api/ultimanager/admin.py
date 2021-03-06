from django.contrib import admin

from ultimanager import models


@admin.register(models.Game)
class GameAdmin(admin.ModelAdmin):
    """
    Admin configuration for the `Game` model.
    """
    fields = ('team', 'opponent', 'starting_position')
    list_display = ('team', 'opponent', 'starting_position')
    search_fields = ('opponent', 'team__name')


@admin.register(models.Player)
class PlayerAdmin(admin.ModelAdmin):
    """
    Admin configuration for the `Player` model.
    """
    fields = ('team', 'name', 'number')
    list_display = ('name', 'number', 'team')
    search_fields = ('name', 'number', 'team')


@admin.register(models.Point)
class PointAdmin(admin.ModelAdmin):
    """
    Admin configuration for the `Point` model.
    """
    fields = ('game', 'starting_position', 'status', 'players')
    list_display = ('game', 'status', 'starting_position')


@admin.register(models.Possession)
class PossessionAdmin(admin.ModelAdmin):
    """
    Admin configuration for the `Possession` model.
    """
    fields = ('point', 'reason', 'defensive_player')
    list_display = ('point', 'reason')


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    """
    Admin configuration for the `Team` model.
    """
    fields = ('name', 'user', 'image')
    list_display = ('name', 'user')
    search_fields = ('name',)


@admin.register(models.Throw)
class ThrowAdmin(admin.ModelAdmin):
    """
    Admin configuration for the `Throw` model.
    """
    fields = ('possession', 'thrower', 'receiver', 'throw_type', 'result')
    list_display = ('possession', 'thrower', 'receiver', 'throw_type')
