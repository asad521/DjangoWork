# Generated by Django 4.0.6 on 2022-08-22 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('page_name', models.CharField(default='Unknown', max_length=90)),
                ('page_cat', models.CharField(default='Unknown', max_length=90)),
                ('page_date', models.DateField()),
            ],
        ),
    ]
