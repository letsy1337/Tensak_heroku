# Generated by Django 3.1.5 on 2021-04-20 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_Tensak', '0002_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='description',
            field=models.CharField(max_length=3000, null=True),
        ),
    ]
