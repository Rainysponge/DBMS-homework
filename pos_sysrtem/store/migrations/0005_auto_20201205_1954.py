# Generated by Django 2.2 on 2020-12-05 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_shop_shop_ownerid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commoditytoshop',
            name='shop_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Shop'),
        ),
        migrations.AlterField(
            model_name='pay',
            name='buyer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pay',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.Order'),
        ),
    ]
