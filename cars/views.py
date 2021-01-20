from django.shortcuts import render, get_object_or_404, redirect
from .models import Car
from .forms import CarForm
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta

# Create your views here.
# CRUDE
# READ all models in DB
def showAllCars(request):
    allert1 = date.today() + timedelta(days=30)
    allert2 = date.today()

    allCars = Car.objects.all()
    return render(request, 'cars.html', {'allCars':allCars, 'allert1':allert1, 'allert2':allert2})

# CREATE new Form for DB
@login_required
def newCar(request):
    flagIfNew = True
    # Check if there are POST or FILES
    form = CarForm(request.POST or None, request.FILES or None)

    # Check if the Form is valid with requirements
    if form.is_valid():
        form.save() # Save Form
        # If Form will be saved, redirect view to cars.html page from showAllCars
        return redirect(showAllCars)

    return  render(request, 'newCar.html', {'form':form, 'new': flagIfNew})

# EDIT Form from DB
@login_required
def editCar(request, id):
    flagIfNew = False
    # get data from DB if valid id or show 404 page
    car = get_object_or_404(Car, pk=id)
    # Fill Form with data from DB on instance
    form = CarForm(request.POST or None, request.FILES or None, instance=car)

    if form.is_valid():
        form.save()
        # If Form will be saved, redirect view to cars.html page from showAllCars
        return redirect(showAllCars)

    return render(request, 'newCar.html', {'form': form, 'new': flagIfNew})

# DELETE Form from DB
@login_required
def deleteCar(request, id):
    car = get_object_or_404(Car, pk=id)

    if request.method == "POST":
        car.delete()
        return redirect(showAllCars)

    return render(request, 'accept.html', {'car': car})




