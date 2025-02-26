# Generated by Django 5.1.6 on 2025-02-25 18:14

import downloader.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="VideoDownload",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.URLField()),
                ("platform", models.CharField(max_length=20)),
                ("title", models.CharField(max_length=255)),
                ("file", models.FileField(upload_to=downloader.models.get_file_path)),
                ("quality", models.CharField(max_length=20)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
