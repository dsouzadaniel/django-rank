from django.urls import path

from .views import HomePageView, saveit, sortit, analysis

urlpatterns = [
    path('ajax/save/', saveit, name='saving_func'),
    path('ajax/sort/', sortit, name='sorting_func'),
    path('analysis/', analysis, name='analyze'),
    path('', HomePageView.as_view(), name='home'),
]