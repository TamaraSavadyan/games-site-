# Generated by Django 4.0.4 on 2022-07-01 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sudoku', '0008_alter_sudoku_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sudoku',
            name='account',
        ),
    ]
