# Generated by Django 3.2.25 on 2024-04-19 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_bookmark_like_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='like_count',
        ),
    ]
