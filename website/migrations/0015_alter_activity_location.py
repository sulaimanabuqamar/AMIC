# Generated by Django 5.0.6 on 2024-07-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_remove_photo_timeline_photo_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
