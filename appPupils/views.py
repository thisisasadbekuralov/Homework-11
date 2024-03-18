from django.shortcuts import render
from .models import Pupil


def students(request):
    student_list = Pupil.objects.all()
    return render(request, 'students.html', {'students': student_list})


def students_details(request, pk):
    student = Pupil.objects.get(id=pk)
    return render(request, 'student_details.html', {'details': student})

