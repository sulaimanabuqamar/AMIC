# Generated by Django 4.2.4 on 2023-10-22 13:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0002_rename_organizingcommitteeteam_committeeteam"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="memberteam",
            name="role",
        ),
    ]
