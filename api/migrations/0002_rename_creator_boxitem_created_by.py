# Generated by Django 4.0.4 on 2022-04-17 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boxitem',
            old_name='creator',
            new_name='created_by',
        ),
    ]
