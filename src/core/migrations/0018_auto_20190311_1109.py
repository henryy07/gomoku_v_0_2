# Generated by Django 2.1.7 on 2019-03-11 11:09

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20190311_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.profile_image_file_path),
        ),
    ]
