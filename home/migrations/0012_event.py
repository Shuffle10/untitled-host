# Generated by Django 3.2.9 on 2021-11-28 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_release_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=400)),
                ('artists', models.CharField(max_length=400)),
                ('ticketPrice', models.IntegerField(null=True)),
            ],
        ),
    ]
