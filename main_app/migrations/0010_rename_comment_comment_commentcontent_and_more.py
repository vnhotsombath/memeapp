# Generated by Django 4.1 on 2022-09-07 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_comment_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='commentcontent',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='meme_id',
            new_name='meme',
        ),
    ]
