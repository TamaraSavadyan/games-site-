# Generated by Django 4.0.4 on 2022-06-30 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_account_balls_account_minesweeper_account_sudoku_and_more'),
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
