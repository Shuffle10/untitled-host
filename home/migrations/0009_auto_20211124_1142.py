# Generated by Django 3.2.9 on 2021-11-24 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_quote_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='image',
        ),
        migrations.AddField(
            model_name='release',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]