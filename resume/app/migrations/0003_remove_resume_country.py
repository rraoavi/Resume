# Generated by Django 4.2.1 on 2024-07-01 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_resume_block_resume_city_resume_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='country',
        ),
    ]
