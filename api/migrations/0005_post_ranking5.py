# Generated by Django 3.2 on 2022-06-12 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20220612_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ranking5',
            field=models.IntegerField(default=10000),
        ),
    ]
