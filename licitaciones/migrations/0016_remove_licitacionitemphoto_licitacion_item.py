# Generated by Django 5.0.2 on 2024-12-28 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licitaciones', '0015_alter_licitacionitemphoto_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='licitacionitemphoto',
            name='licitacion_item',
        ),
    ]