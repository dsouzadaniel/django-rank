from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Record


# Create your views here.

class HomePageView(ListView):
    model = Record
    template_name = 'listrecords.html'
    context_object_name = 'record_list'


@csrf_exempt
def saveit(request):
    new_order = []
    for index, record_pk in enumerate(request.POST.getlist('record[]')):
        new_order.append((index, record_pk))
    request.session['new_order'] = new_order
    return HttpResponse('')


def sortit(request):
    for index, record_pk in request.session['new_order']:
        record = get_object_or_404(Record, pk=int(str(record_pk)))
        record.order = index
        record.save()
    response = redirect('home')
    return response
