# Generated by Django 4.0.3 on 2022-04-01 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messagenode', '0001_initial'),
        ('messagethread', '0002_rename_thread_messagethread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagethread',
            name='messages',
            field=models.ManyToManyField(blank=True, to='messagenode.messagenode'),
        ),
    ]