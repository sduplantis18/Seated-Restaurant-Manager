# Generated by Django 3.1.2 on 2020-11-23 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20201122_1923'),
        ('learning_logs', '0003_auto_20201122_1633'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Seatlocation',
        ),
    ]
