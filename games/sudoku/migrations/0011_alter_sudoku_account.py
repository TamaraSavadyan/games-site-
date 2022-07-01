# Generated by Django 4.0.4 on 2022-07-01 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_alter_account_balls_alter_account_minesweeper_and_more'),
        ('sudoku', '0010_sudoku_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sudoku',
            name='account',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sudoku_game', to='accounts.account'),
        ),
    ]
