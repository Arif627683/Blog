# Generated by Django 2.1.3 on 2018-11-19 11:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20181117_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='image',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
