# Generated by Django 4.0.6 on 2022-07-23 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_alter_account_balls_alter_account_minesweeper_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='balls',
        ),
        migrations.RemoveField(
            model_name='account',
            name='minesweeper',
        ),
        migrations.RemoveField(
            model_name='account',
            name='sudoku',
        ),
        migrations.RemoveField(
            model_name='account',
            name='wordle',
        ),
    ]
