# Generated by Django 2.0.5 on 2018-05-29 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='biography',
            field=models.TextField(default='', help_text='Napisz coś o sobie'),
        ),
    ]
