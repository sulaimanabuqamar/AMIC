# Generated by Django 5.0.6 on 2024-07-22 13:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_alter_photo_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='website.activity'),
        ),
    ]