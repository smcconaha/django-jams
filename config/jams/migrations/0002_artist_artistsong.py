# Generated by Django 4.1.3 on 2022-11-16 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('bio', models.TextField(max_length=500, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArtistSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jams.artist')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jams.song')),
            ],
        ),
    ]
