# Generated by Django 3.2.4 on 2021-06-28 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfile',
            name='owner',
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='authorised_user',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='description',
            field=models.CharField(default='jjjdjdj', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='downloaded',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='file_owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='file_owner', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='identifier',
            field=models.CharField(default='kdddkk', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='mime_type',
            field=models.CharField(default='dff', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='name',
            field=models.CharField(default='ddlddl', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='size_bytes',
            field=models.CharField(default='skssk', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='size_mb',
            field=models.CharField(default='ssss', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='uploaded_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=10)),
                ('comment', models.TextField()),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('file_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_review', to='file.uploadfile')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
