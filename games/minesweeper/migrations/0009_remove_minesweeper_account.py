# Generated by Django 4.0.4 on 2022-07-01 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minesweeper', '0008_alter_minesweeper_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='minesweeper',
            name='account',
        ),
    ]
