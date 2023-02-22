# Generated by Django 3.2 on 2023-02-21 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election_app', '0002_auto_20230220_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='captaincommune',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='captains',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='commune',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalcaptaincommune',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalcaptains',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalcommune',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalleader',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalleaderrespneighborhoods',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalmunicipality',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalneighborhoods',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalpollingstations',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalvoterdata',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='leader',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='leaderrespneighborhoods',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='municipality',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='neighborhoods',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pollingstations',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='voterdata',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]