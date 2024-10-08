# Generated by Django 5.0.6 on 2024-08-02 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Images', models.ImageField(upload_to='posts/')),
                ('category', models.CharField(choices=[('Mental health', 'Mental health'), ('Heart disease', 'Heart disease'), ('Covid 19', 'Covid 19'), ('Immunization', 'Immunization')], max_length=100, null=True)),
                ('Summary', models.TextField()),
                ('Content', models.TextField()),
            ],
        ),
    ]
