# Generated by Django 4.0 on 2023-06-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='publish_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
