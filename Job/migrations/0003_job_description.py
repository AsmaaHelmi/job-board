# Generated by Django 4.1.6 on 2023-02-18 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0002_job_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
