# Generated by Django 4.0.3 on 2022-04-01 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messagenode', '0001_initial'),
        ('person', '0001_initial'),
        ('messagethread', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Thread',
            new_name='MessageThread',
        ),
    ]
