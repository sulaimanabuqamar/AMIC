# Generated by Django 4.2.4 on 2024-07-04 18:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0008_rename_advisorteam_advisor"),
    ]

    operations = [
        migrations.AddField(
            model_name="committee",
            name="team_type",
            field=models.CharField(
                choices=[
                    ("highschool", "High School"),
                    ("junior", "Junior"),
                    ("alumni", "Alumni"),
                ],
                default="highschool",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="head",
            name="team_type",
            field=models.CharField(
                choices=[
                    ("highschool", "High School"),
                    ("junior", "Junior"),
                    ("alumni", "Alumni"),
                ],
                default="highschool",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="team_type",
            field=models.CharField(
                choices=[
                    ("highschool", "High School"),
                    ("junior", "Junior"),
                    ("alumni", "Alumni"),
                ],
                default="highschool",
                max_length=10,
            ),
        ),
    ]
