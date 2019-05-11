from django.urls import path

from .views import HomePageView, sortit

urlpatterns = [
    path('ajax/sort/', sortit, name='sorting_func'),
    path('', HomePageView.as_view(), name='home'),
]