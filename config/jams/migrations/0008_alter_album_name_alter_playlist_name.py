# Generated by Django 4.1.3 on 2022-11-17 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jams', '0007_playlist_rename_albums_song_album_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
