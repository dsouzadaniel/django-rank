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


def analysis(request):
    import numpy as np
    from sklearn.linear_model import LinearRegression

    X = np.array([[12, 1, 4, 5], [1, 2, 6, 7], [24, 2, 1, 1], [2, 3, 3, 2], [6, 6, 3, 2], [5, 3, 2, 4]])
    y = np.array([10, 8, 6, 4, 2, 1])
    reg = LinearRegression().fit(X, y)
    solution = {}
    weights_and_bias = np.append(reg.coef_, [reg.intercept_], axis=0)
    max_coeff = max(weights_and_bias)
    min_coeff = min(weights_and_bias)
    solution['weights'] = [((i - min_coeff) / (max_coeff - min_coeff)) for i in weights_and_bias]


    return render(request, 'analysis.html', context=solution)
