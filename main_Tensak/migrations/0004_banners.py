# Generated by Django 3.1.5 on 2021-04-20 01:49

from django.db import migrations, models
import main_Tensak.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_Tensak', '0003_auto_20210420_0321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to=main_Tensak.models.Banners.get_file_name_banners)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
    ]