# Generated by Django 4.1.1 on 2022-09-06 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_meme_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meme',
            name='url',
        ),
    ]
