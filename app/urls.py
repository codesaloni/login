from django.urls import path
from .views import *
urlpatterns = [
   path('home/',home,name="home"),
   path('doctorlogin/',create_doctor,name="create_doctor"),
   path('doctor/',doctor,name="doctor"),
   path('patientadd/',patient,name="patient"),
   path('Patient/',Patient_create,name="Patient_create"),
   path('post/',post,name="post"),
   path('upload/',upload,name="upload")
]
