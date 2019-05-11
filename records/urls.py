from django.urls import path

from .views import HomePageView, EditRecordView
from .views import saveit, sortit, analysis

urlpatterns = [
    path('ajax/save/', saveit, name='saving_func'),
    path('ajax/sort/', sortit, name='sorting_func'),
    path('analysis/', analysis, name='analyze'),
    path('<int:pk>/edit/', EditRecordView.as_view(), name='edit_record'),
    path('', HomePageView.as_view(), name='home'),
]