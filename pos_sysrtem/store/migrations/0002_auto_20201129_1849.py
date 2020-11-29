# Generated by Django 2.2 on 2020-11-29 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commodity',
            name='commodity_id',
        ),
        migrations.AddField(
            model_name='pay',
            name='POS',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='store.PosInfo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posinfo',
            name='shop_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Shop'),
        ),
    ]
