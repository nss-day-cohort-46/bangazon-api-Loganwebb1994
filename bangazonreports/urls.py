from django.urls import path
from .views import completedorders_list, unpaidorders_list

urlpatterns = [
    path('reports/completedorders', completedorders_list),
    path('reports/unpaidorders', unpaidorders_list),
]
