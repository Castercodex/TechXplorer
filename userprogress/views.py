from django.shortcuts import render, HttpResponseRedirect
from .models import Course, EnrolledCourse, CompletedCourse
# Create your views here.

def dashboard(request):
    courses = Course.objects.all()
    enrolled_courses = EnrolledCourse.objects.all()
    context = {
        "courses": courses,
        "enrolled_courses": enrolled_courses
    }
    return render(request, 'registration/dashboard.html', context)

def add_to_enrolled(response):
    if response.method == "POST":
        form = EnrolledCourse.objects.create(response, course)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = Course(name=n)
            t.save()
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form.EnrolledCourse.objects.create()

    return render(response, "dashboard.html", {"form":form})