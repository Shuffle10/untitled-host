# Generated by Django 3.2.9 on 2021-11-24 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20211124_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]