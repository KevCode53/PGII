# Generated by Django 2.2.5 on 2019-09-08 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0011_auto_20190908_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignacion',
            name='no_asignacion',
        ),
        migrations.AlterField(
            model_name='asignacion',
            name='ingreso_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventario.Ingreso'),
        ),
    ]
