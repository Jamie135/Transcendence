# Generated by Django 4.2.11 on 2024-07-19 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_rename_tournament_tournamentrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamerecord',
            name='hash',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='tournamentrecord',
            name='creation_time',
            field=models.DateTimeField(),
        ),
    ]
