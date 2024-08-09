from django.db import models
from .category import CATEGORY

class Doctor(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    profile_picture=models.ImageField(upload_to='doctor/')
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.IntegerField()

   


    def __str__(self):
        return self.username
    

class Patient(models.Model):
    Patient_first_name=models.CharField(max_length=100)
    Patient_last_name=models.CharField(max_length=100)
    Patient_profile_picture=models.ImageField(upload_to='Patient/')
    Patient_username=models.CharField(max_length=100)
    Patient_email=models.EmailField(max_length=254)
    Patient_password=models.CharField(max_length=100)
    Patient_confirm_password=models.CharField(max_length=100)
    Patient_city=models.CharField(max_length=100)
    Patient_state=models.CharField(max_length=100)
    Patient_pincode=models.IntegerField()



    def __str__(self):
        return self.Patient_username
    
class Post(models.Model):
    Title=models.CharField(max_length=100)
    Images=models.ImageField(upload_to='posts/')
    category = models.CharField(max_length=100, choices=CATEGORY, null=True)
    Summary=models.TextField()
    Content=models.TextField()
    is_draft = models.BooleanField(default=False)



    def __str__(self) :
        return self.category



    
class Book_appointment(models.Model):
    specialty = models.CharField(max_length=50)
    appointment_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    d = models.ForeignKey(Doctor, on_delete=models.CASCADE) 


    def __str__(self) :
        return self.specialty 