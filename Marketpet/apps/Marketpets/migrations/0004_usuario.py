# Generated by Django 4.2.1 on 2023-06-27 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marketpets', '0003_alter_producto_fecha_ingreso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombres', models.IntegerField(primary_key=True, serialize=False)),
                ('apellidos', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
    ]
