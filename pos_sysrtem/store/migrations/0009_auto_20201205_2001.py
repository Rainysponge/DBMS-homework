# Generated by Django 2.2 on 2020-12-05 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commoditytoshop',
            name='commodity_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Commodity'),
        ),
    ]
