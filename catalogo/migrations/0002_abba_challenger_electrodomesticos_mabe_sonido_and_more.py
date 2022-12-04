# Generated by Django 4.1.2 on 2022-11-24 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='abba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=1000)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='challenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=1000)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='electrodomesticos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=1000)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='mabe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=1000)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='sonido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=1000)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='televisores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=1000)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='whirlpool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=1000)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(upload_to='image')),
            ],
        ),
    ]
