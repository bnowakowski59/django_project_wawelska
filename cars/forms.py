from django.forms import ModelForm
from .models import Car

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['marka', 'model', 'nrRejestracyjny', 'rokProdukcji', 'opis', 'obraz']