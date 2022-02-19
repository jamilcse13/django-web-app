# Generated by Django 3.2.8 on 2022-02-19 06:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='il',
            new_name='course_type',
        ),
        migrations.RemoveField(
            model_name='details',
            name='sp',
        ),
        migrations.AddField(
            model_name='allcourses',
            name='started_from',
            field=models.DateField(default=datetime.datetime(2022, 2, 19, 6, 49, 34, 906397, tzinfo=utc), verbose_name='Startted From'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='your_choice',
            field=models.BooleanField(default=False),
        ),
    ]