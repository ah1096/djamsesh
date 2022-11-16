# Generated by Django 4.1.3 on 2022-11-16 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djamsesh', '0011_alter_song_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='genre_id',
        ),
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='djamsesh.artist'),
        ),
    ]
