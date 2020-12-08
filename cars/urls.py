from django.urls import path
from cars.views import showAllCars, newCar, editCar, deleteCar

urlpatterns = [
    path('all/', showAllCars, name='showAllCars'),
    path('new/', newCar, name='newCar'),
    path('edit/<int:id>', editCar, name='editCar'),
    path('delete/<int:id>', deleteCar, name='deleteCAr'),

]