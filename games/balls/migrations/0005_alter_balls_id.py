# Generated by Django 4.0.4 on 2022-06-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balls', '0004_alter_balls_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balls',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
