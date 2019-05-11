from django.shortcuts import render, get_object_or_404
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
def sortit(request):
    for index, record_pk in enumerate(request.POST.getlist('record[]')):
        record = get_object_or_404(Record, pk=int(str(record_pk)))
        record.order = index
        record.save()
    return HttpResponse('')
