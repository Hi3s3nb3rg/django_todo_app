# Generated by Django 3.0.6 on 2020-05-13 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='created',
            new_name='completed',
        ),
    ]
