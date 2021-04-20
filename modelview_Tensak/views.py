from django.shortcuts import render
from main_Tensak.models import *
# Create your views here.

def model_info(request, pk):
    model = Model.objects.get(pk=pk)
    return render(request, 'model_view.html', context={
        'model': model,
    })
