# Generated by Django 3.0.5 on 2020-07-24 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petcare', '0005_auto_20200724_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='warehouseAddress',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]