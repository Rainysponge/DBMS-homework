# Generated by Django 2.2 on 2020-12-03 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20201203_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='shop_ownerID',
        ),
    ]
