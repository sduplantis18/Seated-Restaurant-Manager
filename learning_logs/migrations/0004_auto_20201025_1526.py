# Generated by Django 3.1.2 on 2020-10-25 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_topic_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='address',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='arena_pics'),
        ),
    ]