# Generated by Django 4.1.2 on 2022-12-03 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0010_alter_catalogo_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogo',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
