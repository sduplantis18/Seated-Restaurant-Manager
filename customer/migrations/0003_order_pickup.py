# Generated by Django 3.1.2 on 2021-01-21 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20210118_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pickup',
            field=models.BooleanField(default=True),
        ),
    ]
