# Generated by Django 4.2.4 on 2023-10-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="advisorTeam",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("role", models.CharField(max_length=100)),
                ("about", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="headTeam",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("role", models.CharField(max_length=100)),
                ("about", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="memberTeam",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("role", models.CharField(max_length=100)),
                ("about", models.TextField()),
                ("amicoins", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="organizingcommitteeTeam",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("role", models.CharField(max_length=100)),
                ("about", models.TextField()),
                ("amicoins", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Timeline",
            fields=[
                ("timeline_id", models.AutoField(primary_key=True, serialize=False)),
                ("activity_name", models.CharField(max_length=100)),
                ("activity", models.TextField()),
                ("date", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
            ],
        ),
    ]
