# Generated by Django 5.0 on 2024-11-26 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='img',
            field=models.FileField(max_length=128, upload_to='city', verbose_name='logo'),
        ),
    ]