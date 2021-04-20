from django.shortcuts import render
from .models import Procreator, Model


def main(request):
    procreators = Procreator.objects.filter(is_visible=True).order_by('popular_level')
    for item in procreators:
        item.models = Model.objects.filter(procreator=item.pk)
    return render(request, 'index.html', context={'procreators': procreators})
