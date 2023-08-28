# Generated by Django 3.2.9 on 2021-11-24 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('details', models.TextField()),
            ],
        ),
    ]