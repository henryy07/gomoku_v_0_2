# Generated by Django 2.1.5 on 2019-03-01 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0006_gomokurecordfile_status")]

    operations = [
        migrations.AddField(
            model_name="gomokurecordfile",
            name="url",
            field=models.CharField(default="url", max_length=255),
            preserve_default=False,
        )
    ]