# Generated by Django 5.1.1 on 2024-09-22 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mytable',
            old_name='firstname',
            new_name='firstName',
        ),
    ]
