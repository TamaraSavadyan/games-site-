# Generated by Django 4.0.4 on 2022-06-30 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordle', '0006_alter_wordle_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wordle',
            name='account',
        ),
    ]
