# Generated by Django 4.2.3 on 2023-08-11 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0007_moodtracker_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moodtracker',
            name='date',
        ),
    ]
