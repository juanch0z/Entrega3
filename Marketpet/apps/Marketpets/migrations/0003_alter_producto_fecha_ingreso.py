# Generated by Django 4.2.1 on 2023-06-12 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Marketpets", "0002_alter_producto_fecha_ingreso_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="producto",
            name="fecha_ingreso",
            field=models.DateField(auto_now_add=True),
        ),
    ]
