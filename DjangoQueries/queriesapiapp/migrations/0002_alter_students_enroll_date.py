# Generated by Django 4.0.6 on 2022-08-18 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queriesapiapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='enroll_date',
            field=models.DateTimeField(),
        ),
    ]
