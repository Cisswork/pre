# Generated by Django 4.1.7 on 2023-06-03 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='covid',
            name='prediction_result',
            field=models.BooleanField(default=False),
        ),
    ]
