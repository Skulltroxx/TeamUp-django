# Generated by Django 4.0.6 on 2022-10-24 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_event_arena_alter_event_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='no_of_players',
        ),
    ]
