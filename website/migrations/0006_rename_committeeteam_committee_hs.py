# Generated by Django 4.2.4 on 2024-07-04 17:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0005_rename_headteam_head_hs"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="committeeTeam",
            new_name="committee_HS",
        ),
    ]