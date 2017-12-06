from django.contrib import admin

from ultimanager import models


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    """
    Admin configuration for the `Team` model.
    """
    fields = ('name', 'user', 'image')
    list_display = ('name', 'user')
    search_fields = ('name',)
