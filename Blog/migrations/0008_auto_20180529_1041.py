# Generated by Django 2.0.5 on 2018-05-29 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_auto_20180528_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d'),
        ),
    ]