# Generated by Django 3.2.25 on 2024-04-17 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('profile_image', models.TextField()),
                ('nickname', models.CharField(max_length=24)),
                ('name', models.CharField(max_length=24)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
