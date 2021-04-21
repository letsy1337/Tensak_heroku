from django.shortcuts import render, redirect
from .models import Procreator, Model, Banners, UsersGuideRequests
from .forms import UserGuideRequestsForm, ProcreatorAddForm, ModelAddForm
from django.core.paginator import Paginator

def main(request):
    if request.method == 'POST':
        rent = UserGuideRequestsForm(request.POST)
        if rent.is_valid():
            rent.save()
        return redirect('/')

    procreators = Procreator.objects.filter(is_visible=True).order_by('popular_level')
    procreators_onsale = Procreator.objects.filter(is_visible=True).order_by('popular_level')
    banners = Banners.objects.filter(is_visible=True)
    users_guid_requests = UserGuideRequestsForm()
    for item in procreators:
        item.models = Model.objects.filter(procreator=item.pk, is_sale=False)
    for item in procreators_onsale:
        item.models = Model.objects.filter(procreator=item.pk, is_sale=True)
    return render(request, 'index.html', context={'procreators': procreators,
                                                  'procreators_onsale': procreators_onsale,
                                                  'banners': banners,
                                                  'rent': users_guid_requests,
                                                  })


def addProcreator(request):
    if request.method == 'POST':
        procreatoradd = ProcreatorAddForm(request.POST)
        if procreatoradd.is_valid():
            procreatoradd.save()
        return redirect('/')
    procreators_add = ProcreatorAddForm()
    return render(request, 'procreatoradd.html', context={'procreatoradd': procreators_add,
                                                          })
def addModel(request):
    if request.method == 'POST':
        modeladd = ModelAddForm(request.POST)
        if modeladd.is_valid():
            modeladd.save()
        return redirect('/')
    models_add = ModelAddForm()
    return render(request, 'modeladd.html', context={'modeladd': models_add
                                                     })

def guiderequest(request):
    requests = UsersGuideRequests.objects.filter(is_processed=False).order_by('send_date')
    paginator = Paginator(requests, 10)
    page = request.GET.get('page')
    requests_page = paginator.get_page(page)
    return render(request, 'guide_requests.html', context={'items': requests_page})