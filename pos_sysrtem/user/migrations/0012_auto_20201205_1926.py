# Generated by Django 2.2 on 2020-12-05 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_student_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='IDnumber',
        ),
        migrations.AddField(
            model_name='shopowner',
            name='IDnumber',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]