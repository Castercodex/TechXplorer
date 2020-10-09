from django.shortcuts import render
from .models import C, Cpp, Java, JavaScript, Php, Python
# Create your views here.

def c_course(request):
    context = {
        'course': C.objects.all()
    }
    return render(request, 'home.html', context)
