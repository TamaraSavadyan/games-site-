# Generated by Django 4.0.4 on 2022-07-01 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_remove_account_balls_remove_account_minesweeper_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
    ]
