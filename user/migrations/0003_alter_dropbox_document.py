# Generated by Django 3.2.7 on 2022-01-03 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_dropbox'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dropbox',
            name='document',
            field=models.FileField(max_length=10000, upload_to=''),
        ),
    ]
