# Generated by Django 4.0.4 on 2022-06-08 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balls', '0002_alter_balls_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balls',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='balls',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]