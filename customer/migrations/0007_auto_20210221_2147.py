# Generated by Django 3.1.2 on 2021-02-22 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20210221_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seatlocation',
            name='seat',
            field=models.IntegerField(null=True),
        ),
    ]
