# Generated by Django 4.2.11 on 2024-05-29 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_transcendence', '0005_gamerecord_player1_score_gamerecord_player2_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='avatar',
            field=models.ImageField(default='avatars/default.jpg', upload_to='avatars/'),
        ),
    ]