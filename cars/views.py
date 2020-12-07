from django.shortcuts import render
from .models import Car


# Create your views here.

def showAllCars(request):
    allCars = Car.objects.all()
    return  render(request, 'cars.html', {'allCars':allCars})

