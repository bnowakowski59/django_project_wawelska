from django.contrib import admin
from django.urls import path
from cars.views import showAllCars

urlpatterns = [
    path('all/', showAllCars),
]