from django.shortcuts import render
from django.views.generic import ListView

from .models import Record
# Create your views here.

class HomePageView(ListView):
    model = Record
    template_name = 'listrecords.html'
    context_object_name = 'record_list'
