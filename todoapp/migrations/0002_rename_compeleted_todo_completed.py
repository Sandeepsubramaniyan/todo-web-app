# Generated by Django 4.1.3 on 2022-11-20 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='compeleted',
            new_name='completed',
        ),
    ]