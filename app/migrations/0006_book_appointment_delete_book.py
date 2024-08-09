# Generated by Django 5.0.6 on 2024-08-07 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.CharField(max_length=50)),
                ('appointment_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
