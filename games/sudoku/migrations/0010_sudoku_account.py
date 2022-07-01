# Generated by Django 4.0.4 on 2022-07-01 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_account_balls_account_minesweeper_account_sudoku_and_more'),
        ('sudoku', '0009_remove_sudoku_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='sudoku',
            name='account',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='sudoku_game', to='accounts.account'),
            preserve_default=False,
        ),
    ]