# Generated by Django 3.1.5 on 2021-04-20 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_Tensak', '0004_banners'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='procreator',
            name='is_sale',
        ),
        migrations.AddField(
            model_name='model',
            name='is_sale',
            field=models.BooleanField(default=False),
        ),
    ]