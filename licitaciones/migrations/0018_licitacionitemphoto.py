# Generated by Django 5.0.2 on 2024-12-29 00:44

import django.db.models.deletion
import licitaciones.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licitaciones', '0017_delete_licitacionitemphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='LicitacionItemPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to=licitaciones.models.user_path)),
                ('licitacion_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licitaciones.licitacionitem')),
            ],
        ),
    ]