# Generated by Django 4.2.1 on 2023-06-12 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Marketpets", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="producto", name="fecha_ingreso", field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="producto",
            name="fecha_vencimiento",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="producto",
            name="image_url",
            field=models.ImageField(upload_to="imagenesProductos"),
        ),
    ]
