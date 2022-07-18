# Generated by Django 4.0.5 on 2022-07-15 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(db_column='term', max_length=200)),
                ('uid', models.CharField(db_column='uid', max_length=200)),
                ('lat', models.FloatField(db_column='lat')),
                ('lng', models.FloatField(db_column='lng')),
                ('type', models.CharField(db_column='type', max_length=200)),
                ('state', models.CharField(db_column='state', max_length=200)),
            ],
            options={
                'db_table': 'listingsAndReviews',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ListingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=200)),
                ('room_type', models.CharField(db_column='room_type', max_length=200)),
                ('price', models.FloatField(db_column='price')),
                ('summary', models.CharField(db_column='summary', max_length=200)),
            ],
        ),
    ]