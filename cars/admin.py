from django.contrib import admin
from .models import Car

# Register your models here.
admin.site.register(Car)


# @admin.register(Car)
# class CarAdmin(admin.ModelAdmin):
#
#     # fields = ["obraz", "marka", "model", "nrRejestracyjny"]
#     # list_display = ["marka", "model"]
#     # list_filter =  ["marka"]
#     search_fields = ["nrRejestracyjny"]