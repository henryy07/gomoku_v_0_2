# Generated by Django 2.1.5 on 2019-02-02 13:08

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="picture",
            field=models.ImageField(
                default="default.jpg", upload_to=core.models.profile_image_file_path
            ),
        )
    ]
