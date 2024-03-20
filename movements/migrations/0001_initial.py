# Generated by Django 4.2 on 2024-03-20 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0004_equipment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateField(auto_now=True, null=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('reference', models.CharField(help_text='\n      Field for the Document No. that will\n      serve as a reference for the purchase\n      or donation\n    ', max_length=250, verbose_name='Reference')),
                ('state', models.BooleanField(default=False, verbose_name='Available')),
                ('description', models.TextField(default='S/D', verbose_name='Description')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'Entries',
                'verbose_name_plural': 'Entriess',
            },
        ),
        migrations.CreateModel(
            name='MaterialEntryDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateField(auto_now=True, null=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('quantity', models.PositiveSmallIntegerField(default=1, verbose_name='Quantity')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Amount')),
                ('location', models.CharField(blank=True, max_length=250, null=True, verbose_name='Location')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('id_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movements.entry')),
                ('id_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.material', verbose_name='Material')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'MaterialEntryDetail',
                'verbose_name_plural': 'MaterialEntryDetails',
            },
        ),
    ]
