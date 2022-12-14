# Generated by Django 4.1.2 on 2022-11-07 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('marca', models.CharField(max_length=40, verbose_name='Marca')),
                ('descripcion', models.TextField(null=True, verbose_name='Marca')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen')),
            ],
        ),
    ]
