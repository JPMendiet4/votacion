# Generated by Django 3.2 on 2023-02-22 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election_app', '0005_auto_20230222_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalmunicipality',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Activo'),
        ),
        migrations.AlterField(
            model_name='municipality',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Activo'),
        ),
    ]