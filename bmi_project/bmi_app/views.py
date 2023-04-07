import subprocess

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'bmi/home.html')

def calculate_bmi(request):
    if request.method == 'POST':
        height = float(request.POST['height']) / 100  # Convert cm to m
        weight = float(request.POST['weight'])

        # Execute the BMI_cer508.cpp program and capture its output
        output = subprocess.check_output(['bmi_project/BMI_cer508.cpp', str(height), str(weight)])

        # Decode the output from bytes to a string
        bmi = float(output.decode().strip())

        context = {
            'bmi': bmi,
        }

        return render(request, 'bmi/result.html', context)
    else:
        return HttpResponse('Method Not Allowed')
