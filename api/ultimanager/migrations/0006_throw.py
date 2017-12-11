# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 10:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ultimanager', '0005_possession'),
    ]

    operations = [
        migrations.CreateModel(
            name='Throw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(choices=[('C', 'Completion'), ('G', 'Goal'), ('T', 'Turnover')], help_text='The result of the throw.', max_length=1)),
                ('throw_type', models.CharField(choices=[('B', 'Backhand'), ('F', 'Forehand'), ('O', 'Other')], help_text='The type of the throw.', max_length=1)),
                ('possession', models.ForeignKey(help_text='The possession the throw is a part of.', on_delete=django.db.models.deletion.CASCADE, related_name='throws', related_query_name='throw', to='ultimanager.Possession')),
                ('receiver', models.ForeignKey(help_text='The player who received the pass.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_throws', related_query_name='received_throw', to='ultimanager.Player')),
                ('thrower', models.ForeignKey(help_text='The player who threw the pass.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='throws', related_query_name='throw', to='ultimanager.Player')),
            ],
            options={
                'verbose_name_plural': 'throws',
                'verbose_name': 'throw',
            },
        ),
    ]
