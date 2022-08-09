# Generated by Django 4.0.6 on 2022-08-09 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_remove_account_balls_remove_account_minesweeper_and_more'),
        ('wordle', '0014_alter_wordle_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordle',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wordle_game', to='accounts.account'),
        ),
    ]
