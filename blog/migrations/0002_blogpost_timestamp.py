# Generated by Django 2.2.6 on 2019-10-16 18:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 16, 18, 11, 32, 122355, tzinfo=utc)),
        ),
    ]