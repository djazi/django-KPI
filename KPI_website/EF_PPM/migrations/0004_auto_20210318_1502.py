# Generated by Django 3.1.7 on 2021-03-18 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EF_PPM', '0003_auto_20210318_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production_nc',
            name='ID_prod_NC',
            field=models.IntegerField(),
        ),
    ]