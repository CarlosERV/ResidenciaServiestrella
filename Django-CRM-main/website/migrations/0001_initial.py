# Generated by Django 4.1.7 on 2023-02-16 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('RFC', models.CharField(max_length=50)),
                ('Equipo', models.CharField(max_length=20)),
                ('Marca', models.CharField(max_length=20)),
                ('Modelo', models.CharField(max_length=20)),
                ('NoSerie', models.CharField(max_length=20)),
                ('Lectura', models.CharField(max_length=20)),
                ('Observaciones', models.CharField(max_length=100)),
                ('Descripcion', models.CharField(max_length=100)),
                ('PUnitario', models.CharField(max_length=20)),
                ('Importe', models.CharField(max_length=20)),
                ('SubTotal', models.CharField(max_length=20)),
                ('Iva', models.CharField(max_length=20)),
                ('Total', models.CharField(max_length=20)),

                
            ],
        ),
    ]
