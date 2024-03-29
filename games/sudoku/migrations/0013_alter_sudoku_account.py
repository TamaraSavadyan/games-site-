# Generated by Django 4.0.4 on 2022-07-01 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_alter_account_balls_alter_account_minesweeper_and_more'),
        ('sudoku', '0012_alter_sudoku_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sudoku',
            name='account',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='sudoku_game', to='accounts.account'),
            preserve_default=False,
        ),
    ]
