# Generated by Django 5.0.2 on 2024-12-27 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licitaciones', '0011_remove_licitacionitemphoto_licitacion_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licitacionitem',
            name='photos',
            field=models.ManyToManyField(blank=True, null=True, to='licitaciones.licitacionitemphoto'),
        ),
    ]
