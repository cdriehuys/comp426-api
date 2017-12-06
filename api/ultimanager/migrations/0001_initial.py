# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 03:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, help_text="The team's logo.", null=True, upload_to='images/teams/')),
                ('name', models.CharField(help_text="The team's name.", max_length=255)),
                ('user', models.ForeignKey(help_text='The user who manages the team.', on_delete=django.db.models.deletion.CASCADE, related_name='teams', related_query_name='team', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'teams',
                'verbose_name': 'team',
            },
        ),
    ]