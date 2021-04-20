# Generated by Django 3.1.5 on 2021-04-19 23:45

from django.db import migrations, models
import django.db.models.deletion
import main_Tensak.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_Tensak', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('is_visible', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=300, null=True)),
                ('photo', models.ImageField(upload_to=main_Tensak.models.Model.get_file_name_dishes)),
                ('procreator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_Tensak.procreator')),
            ],
        ),
    ]