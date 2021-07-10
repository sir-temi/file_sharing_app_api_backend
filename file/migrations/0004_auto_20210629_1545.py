# Generated by Django 3.2.4 on 2021-06-29 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0003_rename_name_uploadfile_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='restricted_by_country',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='restricted_by_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
