# Generated by Django 2.1.3 on 2019-01-08 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190108_1200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='backup',
            old_name='user_id',
            new_name='user',
        ),
    ]
