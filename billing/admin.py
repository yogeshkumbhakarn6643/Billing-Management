from django.contrib import admin
from .models import Invoice, MeterReading, Customer

model = (
    Invoice, MeterReading, Customer
)
admin.site.register(model)
# Register your models here.