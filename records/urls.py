from django.urls import path

from .views import HomePageView, saveit, sortit

urlpatterns = [
    path('ajax/save/', saveit, name='saving_func'),
    path('ajax/sort/', sortit, name='sorting_func'),
    path('', HomePageView.as_view(), name='home'),
]