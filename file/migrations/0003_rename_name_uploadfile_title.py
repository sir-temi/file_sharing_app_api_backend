# Generated by Django 3.2.4 on 2021-06-29 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_auto_20210628_2154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadfile',
            old_name='name',
            new_name='title',
        ),
    ]
