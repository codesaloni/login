from django.contrib import admin
from .models import *

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','profile_picture','username','email','password','confirm_password','city','state','pincode']
   


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display=['Patient_first_name','Patient_last_name','Patient_profile_picture','Patient_username','Patient_email','Patient_password','Patient_confirm_password','Patient_city','Patient_state','Patient_pincode']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['Title','Images','category','Summary','Content']


@admin.register(Book_appointment)
class BookAdmin(admin.ModelAdmin):
    list_display=['id','specialty','appointment_date','start_time','end_time']