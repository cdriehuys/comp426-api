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


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    """
    Admin configuration for the `Team` model.
    """
    fields = ('name', 'user', 'image')
    list_display = ('name', 'user')
    search_fields = ('name',)
