# Generated by Django 2.2 on 2020-12-09 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_shop_shop_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='contends',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
