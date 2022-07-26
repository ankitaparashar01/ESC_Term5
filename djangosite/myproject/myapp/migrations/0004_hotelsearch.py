# Generated by Django 4.0.5 on 2022-07-26 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_destinationcat_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destinationorhotel', models.CharField(blank=True, default='-', max_length=300)),
                ('calendarCheckin', models.DateField(blank=True)),
                ('calendarCheckout', models.DateField(blank=True)),
                ('roomsnumber', models.PositiveIntegerField(blank=True)),
                ('adultsnumber', models.PositiveIntegerField(blank=True)),
                ('childrennumber', models.PositiveIntegerField(blank=True)),
            ],
        ),
    ]
