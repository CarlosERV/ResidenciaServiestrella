# Generated by Django 5.0.3 on 2024-04-22 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_record_descripcion_alter_record_equipo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bitacor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('rfc', models.CharField(max_length=50)),
                ('razonS', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=20)),
                ('cuidad', models.CharField(max_length=100)),
                ('cp', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('nserie', models.CharField(max_length=50)),
                ('funciones', models.CharField(max_length=50)),
                ('servicio', models.CharField(max_length=50)),
                ('costo', models.CharField(max_length=50)),
                ('moneda', models.CharField(max_length=50)),
                ('procesos', models.CharField(max_length=50)),
                ('excedente', models.CharField(max_length=50)),
                ('observaciones', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='record',
            name='Lectura',
            field=models.CharField(max_length=50),
        ),
    ]
