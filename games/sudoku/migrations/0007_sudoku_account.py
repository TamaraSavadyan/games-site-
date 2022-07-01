# Generated by Django 4.0.4 on 2022-06-30 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_account_id'),
        ('sudoku', '0006_remove_sudoku_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='sudoku',
            name='account',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sudoku_game', to='accounts.account'),
            preserve_default=False,
        ),
    ]