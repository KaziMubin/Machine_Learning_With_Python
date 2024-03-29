# Generated by Django 4.2.9 on 2024-01-19 01:54

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserInfo",
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
                ("Name", models.CharField(max_length=120)),
                ("Age", models.IntegerField()),
                ("Sex", models.IntegerField()),
                ("BP", models.IntegerField()),
                ("Cholesterol", models.IntegerField()),
                ("Na_to_K", models.FloatField()),
                ("Time", models.DateTimeField(auto_now_add=True)),
                ("Prediction", models.CharField(max_length=20)),
            ],
        ),
    ]
