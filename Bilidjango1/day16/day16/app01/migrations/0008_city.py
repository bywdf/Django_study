# Generated by Django 5.0 on 2024-11-26 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_boss'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('count', models.IntegerField(verbose_name='人口')),
                ('img', models.FileField(max_length=128, upload_to='', verbose_name='logo')),
            ],
        ),
    ]
