# Generated by Django 4.0.6 on 2022-08-24 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('one2onerelationshipapp', '0005_alter_page_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='user',
            field=models.OneToOneField(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
