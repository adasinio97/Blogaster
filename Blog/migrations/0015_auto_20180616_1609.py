# Generated by Django 2.0.5 on 2018-06-16 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0014_auto_20180603_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]