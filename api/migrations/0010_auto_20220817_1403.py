# Generated by Django 3.2 on 2022-08-17 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_group_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='streaming1',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='streaming2',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='streaming3',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='streaming4',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='streaming5',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
