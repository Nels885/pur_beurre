# Generated by Django 2.1.3 on 2019-01-10 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('save', '0002_auto_20190110_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backup',
            name='search_product',
        ),
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
