# Generated by Django 4.0.4 on 2022-06-30 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_account_id'),
        ('wordle', '0007_remove_wordle_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordle',
            name='account',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='wordle_game', to='accounts.account'),
            preserve_default=False,
        ),
    ]
