# Generated by Django 4.1.3 on 2022-11-17 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djamsesh', '0002_genre_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coverURL', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
