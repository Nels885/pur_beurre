# Generated by Django 2.1.3 on 2019-01-10 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190110_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backup',
            name='subs_product',
        ),
        migrations.RemoveField(
            model_name='backup',
            name='user',
        ),
        migrations.DeleteModel(
            name='Backup',
        ),
    ]
