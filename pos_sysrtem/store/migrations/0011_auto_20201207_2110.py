# Generated by Django 2.2 on 2020-12-07 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20201205_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pay',
            name='order_id',
        ),
        migrations.AddField(
            model_name='order',
            name='pay',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='store.Pay'),
        ),
    ]