# Generated by Django 3.2 on 2023-02-22 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('election_app', '0007_auto_20230222_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalvoterdata',
            old_name='names',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='voterdata',
            old_name='names',
            new_name='name',
        ),
    ]
