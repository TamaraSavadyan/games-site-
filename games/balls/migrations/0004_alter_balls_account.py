# Generated by Django 4.0.4 on 2022-06-08 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_account_balls_alter_account_minesweeper_and_more'),
        ('balls', '0003_alter_balls_score_alter_balls_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balls',
            name='account',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='balls_game', to='accounts.account'),
        ),
    ]