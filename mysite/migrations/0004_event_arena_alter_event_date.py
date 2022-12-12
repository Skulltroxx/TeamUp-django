# Generated by Django 4.0.6 on 2022-10-24 07:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_arena'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='arena',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mysite.arena'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.date(2022, 10, 31)),
        ),
    ]