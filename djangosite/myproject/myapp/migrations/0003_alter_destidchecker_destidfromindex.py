# Generated by Django 4.0.5 on 2022-08-02 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_api3usehotelid_destidchecker_hotelsearch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destidchecker',
            name='destIdFromIndex',
            field=models.CharField(max_length=200),
        ),
    ]
