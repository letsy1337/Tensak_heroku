from django.db import models
from uuid import uuid4
import os


class Procreator(models.Model):
    title = models.CharField(max_length=50)
    popular_level = models.IntegerField()
    is_visible = models.BooleanField(default=True)
    is_sale = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'


class Model(models.Model):
    def get_file_name_dishes(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return os.path.join('images/models/', filename)

    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    description = models.CharField(max_length=3000, null=True)
    photo = models.ImageField(upload_to=get_file_name_dishes)
    procreator = models.ForeignKey(Procreator, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.procreator} - {self.title}'


class Banners(models.Model):
    def get_file_name_banners(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return os.path.join('images/banners/', filename)

    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=get_file_name_banners)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'
