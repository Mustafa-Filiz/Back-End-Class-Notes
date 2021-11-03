from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {
        'title' : "Clarusway",
        'dict_1' : { 'Django' : 'Framework'},
        'my_list' : [2, 3, 4]
    }
    return render(request, 'app/home.html', context)