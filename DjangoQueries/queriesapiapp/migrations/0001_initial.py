# Generated by Django 4.0.6 on 2022-08-18 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown', max_length=15)),
                ('roll', models.IntegerField(default=0, unique=True)),
                ('city', models.CharField(default='Unknown', max_length=20)),
                ('marks', models.IntegerField(default=0)),
                ('pass_date', models.DateField()),
                ('enroll_date', models.DateTimeField(default='1992-12-30 23:59:59')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown', max_length=15)),
                ('emp_num', models.IntegerField(default=0, unique=True)),
                ('city', models.CharField(default='Unknown', max_length=20)),
                ('salary', models.IntegerField(default=0)),
                ('join_date', models.DateField()),
            ],
        ),
    ]