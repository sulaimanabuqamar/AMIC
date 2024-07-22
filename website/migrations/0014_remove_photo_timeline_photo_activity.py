# Generated by Django 5.0.6 on 2024-07-22 10:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_remove_activity_id_activity_activity_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='timeline',
        ),
        migrations.AddField(
            model_name='photo',
            name='activity',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='website.activity'),
            preserve_default=False,
        ),
    ]
