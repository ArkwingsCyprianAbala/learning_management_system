# Generated by Django 4.1.1 on 2022-09-27 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0005_event'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
    ]
