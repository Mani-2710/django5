# Generated by Django 4.2.4 on 2023-11-03 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NatalChartAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='guest', max_length=100)),
                ('birth_date', models.DateField()),
                ('birth_time', models.TimeField()),
                ('birth_place', models.CharField(max_length=100)),
            ],
        ),
    ]
