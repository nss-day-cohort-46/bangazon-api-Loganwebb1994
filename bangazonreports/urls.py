from django.urls import path
from .views import completedorders_list

urlpatterns = [
    path('reports/completedorders', completedorders_list),
]
