# Generated by Django 4.1.3 on 2022-11-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djamsesh', '0009_alter_album_id_alter_artist_id_alter_genre_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
