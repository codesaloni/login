# Generated by Django 5.0.6 on 2024-08-07 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_book_delete_book_appointment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Book_appointment',
        ),
    ]
