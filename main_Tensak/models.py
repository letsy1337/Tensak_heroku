from django.db import models


class Procreator(models.Model):
    title = models.CharField(max_length=50)
    popular_level = models.IntegerField()
    is_visible = models.BooleanField(default=True)
    is_sale = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'
