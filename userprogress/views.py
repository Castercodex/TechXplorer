from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Course, EnrolledCourse, CompletedCourse


# Create your views here.


def dashboard(request):
    courses = Course.objects.all()
    enrolled_courses = EnrolledCourse.objects.all()
    context = {"courses": courses, "enrolled_courses": enrolled_courses}
    return render(request, "registration/dashboard.html", context)


def add_to_enrolled(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrolled_course, created = EnrolledCourse.objects.get_or_create(
        course=course,
        user=request.user,
    )
    # enrolled_qs = EnrolledCourse.objects.filter()
    # # if enrolled_qs.exists():
    # #     enrolled = enrolled_qs
    # #     # check if the order item is in the order
    # #     if enrolled.filter(course__slug=course.slug).exists():
    # #         messages.info(request, "This item quantity Exist")
    # #         # return redirect("core:order-summary")
    # #     else:
    # #         enrolled.course.add(enrolled_course)
    # #         messages.info(request, "This item was added to your cart.")
    # # else:
    # #     enrolled_date = timezone.now()
    # #     enrolled = EnrolledCourse.objects.create(
    # #         user=request.user, enrolled_date=enrolled_date
    # #     )
    # #     enrolled.course.add(enrolled_course)
    # #     messages.info(request, "This item was added to your cart.")
    return HttpResponseRedirect(redirect_to="/dashboard")
