# Generated by Django 4.0.4 on 2022-04-17 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_creator_boxitem_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boxitem',
            old_name='created_by',
            new_name='creator',
        ),
    ]
