from django.urls import path
from .views import students, students_details

urlpatterns = [
    path('', students, name='students'),
    path('students/<int:pk>', students_details, name='students_details')
]