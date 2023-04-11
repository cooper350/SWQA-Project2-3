import subprocess
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST

def determine_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 24.9 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def home(request):
    if request.method == 'POST':
        height_ft = int(request.POST['feet'])
        height_in = int(request.POST['inches'])
        weight_lbs = float(request.POST['weight'])

        # Execute the BMI_cer508.cpp program and capture its output
        output = subprocess.check_output(['./bmi_executable', str(height_ft), str(height_in), str(weight_lbs)])

        # Decode the output from bytes to a string
        bmi = float(output.decode().strip())
        category = determine_category(bmi)

        context = {
            'bmi': bmi,
            'category': category,
        }

        return render(request, 'bmi_app/bmi.html', context)
    else:
        return render(request, 'bmi_app/bmi.html')
