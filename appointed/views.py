from django.shortcuts import render

# Create your views here.
from .models import VaccCenter, Patient

def vaccCenter_list(request):
    vaccCenter = VaccCenter.objects.all()
    return render(request, 'appointed/vaccCenter_list.html', {'Vaccine Distribution Center': vaccCenter})

def patient_list(request):
    patient = Patient.objects.all()
    return render(request, 'appointed/patient_list.html', {'Patient Information': patient })
    