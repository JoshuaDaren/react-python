# Generated by Django 3.2 on 2022-06-19 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_post_ranking5'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/banners'),
        ),
    ]
