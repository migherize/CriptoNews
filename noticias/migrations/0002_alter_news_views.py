# Generated by Django 4.0.5 on 2022-06-29 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='views',
            field=models.BigIntegerField(),
        ),
    ]
