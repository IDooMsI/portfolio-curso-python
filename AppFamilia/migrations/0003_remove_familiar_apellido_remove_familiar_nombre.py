# Generated by Django 4.1 on 2022-08-30 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppFamilia', '0002_familiar_delete_familia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familiar',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='familiar',
            name='nombre',
        ),
    ]
