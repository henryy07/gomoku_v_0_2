# Generated by Django 2.1.7 on 2019-03-07 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("core", "0015_auto_20190307_1907")]

    operations = [
        migrations.AlterField(
            model_name="gomokurecord",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users_games",
                to=settings.AUTH_USER_MODEL,
            ),
        )
    ]