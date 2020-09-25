from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from student.models import Attendnce



def landing(request):
    if request.method == "POST":
        student_name = request.POST.get('sname', '')
        student_id = request.POST.get('sid', '')
        student = Attendnce(student_name=student_name, student_id=student_id)
        student.save()
        return render(request, 'quiz.html')

    return render(request, 'index.html')


def score(request):
    return render(request, 'index.html')
