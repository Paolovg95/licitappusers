# Generated by Django 5.0.2 on 2024-12-28 19:50

import licitaciones.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licitaciones', '0014_remove_licitacionitemphoto_licitacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licitacionitemphoto',
            name='photo',
            field=models.ImageField(blank=True, default=1, null=True, upload_to=licitaciones.models.user_path),
        ),
    ]
