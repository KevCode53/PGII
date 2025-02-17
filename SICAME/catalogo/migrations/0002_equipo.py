# Generated by Django 2.2.5 on 2019-10-03 15:38

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', ckeditor.fields.RichTextField(default='S/D', verbose_name='Descripcion')),
                ('img', models.ImageField(blank=True, null=True, upload_to='Catalogo/', verbose_name='Imagen')),
                ('id_e', models.CharField(max_length=15)),
                ('identificador', models.CharField(default='I', max_length=3, verbose_name='')),
                ('cat', models.CharField(max_length=3, verbose_name='')),
                ('orden', models.CharField(max_length=5, verbose_name='')),
                ('id_Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Categoria', verbose_name='Categoria')),
                ('id_Marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Marca', verbose_name='Marca')),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
            },
        ),
    ]
