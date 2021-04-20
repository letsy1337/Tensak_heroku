from django.urls import path
from .views import main, addProcreator, addModel

urlpatterns = [
    path('', main, name='Main View'),
    path('procreatoradd', addProcreator, name='Add Procreator'),
    path('modeladd', addModel, name='Add Model')
]