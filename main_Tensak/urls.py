from django.urls import path
from .views import main, addProcreator, addModel,guiderequest

urlpatterns = [
    path('', main, name='Main View'),
    path('procreatoradd', addProcreator, name='Add Procreator'),
    path('modeladd', addModel, name='Add Model'),
    path('guiderequests/', guiderequest, name='View guide requests')
]