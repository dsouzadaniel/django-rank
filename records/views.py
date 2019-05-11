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
    def softmax(x):
        """Compute softmax values for each sets of scores in x."""
        return np.exp(x) / np.sum(np.exp(x), axis=0)

    import numpy as np
    from sklearn.linear_model import LinearRegression
    X = []
    y = []
    ranked_weights = {
        '0': 10,
        '1': 8,
        '2': 6,
        '3': 4,
        '4': 2,
        '5': 1,
    }

    for single_record in Record.objects.all():
        X.append([single_record.feature_a,
                  single_record.feature_b,
                  single_record.feature_c,
                  single_record.feature_d,
                  single_record.feature_e
                  ])
        y.append(ranked_weights[str(single_record.order)])

    X = np.array(X)
    y = np.array(y)
    #
    # X = np.array([[12, 1, 4, 5], [1, 2, 6, 7], [24, 2, 1, 1], [2, 3, 3, 2], [6, 6, 3, 2], [5, 3, 2, 4]])
    # y = np.array([10, 8, 6, 4, 2, 1])
    reg = LinearRegression().fit(X, y)
    weights = reg.coef_

    solution = {}
    solution['X'] = X
    solution['y'] = y
    feature_names = ['Adverse Effect',
                     'Identifiable Patient',
                     'Drug',
                     'Precondition',
                     'MAH'
                     ]
    softmax_weights = [str(round(i*100, 2))for i in softmax(weights)]
    solution['output'] = zip(feature_names, softmax_weights)

    return render(request, 'analysis.html', context=solution)
