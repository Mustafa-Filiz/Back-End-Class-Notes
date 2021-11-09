from django.shortcuts import redirect, render
from .models import Student
from .forms import StudentForm

# Create your views here.

def home(request):
    return render(request, "fscohort/home.html")

def student_list(request):
    students = Student.objects.all()
    context = {
		"students" : students
	}
    return render(request, "fscohort/student_list.html", context)

def student_add(request):
    form = StudentForm
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("/student_add")
    
    context = {
		"form" : form 
	}
    
    return render(request, "fscohort/student_add.html", context)

def student_detail(request):
    pass

def student_update(request):
    pass

def student_delete(request):
    pass

