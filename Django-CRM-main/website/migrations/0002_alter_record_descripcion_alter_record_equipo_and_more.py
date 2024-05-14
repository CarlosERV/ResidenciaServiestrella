# Generated by Django 5.0.3 on 2024-03-29 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='Descripcion',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='Equipo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='Importe',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='Iva',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='Lectura',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='Marca',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='Modelo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='NoSerie',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='Observaciones',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='PUnitario',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='SubTotal',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='Total',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
