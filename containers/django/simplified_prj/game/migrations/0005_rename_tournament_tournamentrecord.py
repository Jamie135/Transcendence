# Generated by Django 4.2.11 on 2024-07-14 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_delete_game'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tournament',
            new_name='TournamentRecord',
        ),
    ]
