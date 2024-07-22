# Generated by Django 5.0.6 on 2024-07-22 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_alter_activity_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='website.timeline'),
        ),
    ]