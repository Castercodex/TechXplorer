from django.contrib import admin
from .models import Course, CompletedCourse, EnrolledCourse
# Register your models here.

admin.site.register(Course)
admin.site.register(CompletedCourse)
admin.site.register(EnrolledCourse)