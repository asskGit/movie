# Generated by Django 5.0 on 2024-01-23 11:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asmovie', '0003_genre_remove_movie_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movie', to='asmovie.genre'),
        ),
    ]
