# Generated by Django 2.0.5 on 2018-05-29 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_profile_biography'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='biography',
            field=models.TextField(blank=True, help_text='Napisz coś o sobie', null=True),
        ),
    ]
