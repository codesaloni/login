from django.shortcuts import render, redirect
from .models import Doctor,Patient
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth import get_user_model

User = get_user_model()  

def create_doctor(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        profile_picture = request.FILES.get('profile_picture') 

        

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('create_doctor')

        user=Doctor.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
            confirm_password=confirm_password,
            city=city,
            state=state,
            pincode=pincode,
            profile_picture=profile_picture
        )
        user.save()
        
        return redirect('doctor')

    return render(request, 'doctorlogin.html',{})

def doctor(request):
    items=Doctor.objects.all()
    content={
        'items':items
    }
    return render(request,'doctor.html',content)



def home(request):
    return render(request,"home.html",{})

def Patient_create(request):
    if request.method == 'POST':
        Patient_first_name = request.POST.get('Patient_first_name')
        Patient_last_name = request.POST.get('Patient_last_name')
        Patient_username = request.POST.get('Patient_username')
        Patient_email = request.POST.get('Patient_email')
        Patient_password = request.POST.get('Patient_password')
        Patient_confirm_password = request.POST.get('Patient_confirm_password')
        Patient_city = request.POST.get('Patient_city')
        Patient_state = request.POST.get('Patient_state')
        Patient_pincode = request.POST.get('Patient_pincode')
        Patient_profile_picture = request.FILES.get('Patient_profile_picture') 

        # print(f"Received data: {first_name}, {last_name}, {username}, {email}, {password}, {confirm_password}, {city}, {state}, {pincode}")

        if Patient_password != Patient_confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('create_doctor')

        pro=Patient.objects.create(
            Patient_first_name=Patient_first_name,
            Patient_last_name=Patient_last_name,
            Patient_username=Patient_username,
            Patient_email=Patient_email,
            Patient_password=Patient_password,
            Patient_confirm_password=Patient_confirm_password,
            Patient_city=Patient_city,
            Patient_state=Patient_state,
            Patient_pincode=Patient_pincode,
            Patient_profile_picture=Patient_profile_picture
        )
        pro.save()
        return redirect('patient')

    return render(request,"Patientsignup.html",{})

def patient(request):
    items=Patient.objects.all()
    context={
        'items':items
    }
    return render(request,"patient.html",context)