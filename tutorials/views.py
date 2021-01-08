from django.shortcuts import render
from .models import C, Cpp, Java, JavaScript, Php, Python

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from userprogress.models import Course
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
# Create your views here.


def home_view(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    return render(request, "home.html", context)

class PhpList(ListView):
    model = Php
    template_name = './courses/php.html'
    context_object_name = 'queryset'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        php = Php.objects.all()
        queryset = Php
        context = super().get_context_data(**kwargs)
        context['page_request_var'] = "page"
        context['php'] = php
        return context
    

class PythonList(ListView):
    model = Python
    template_name = './courses/python.html'
    context_object_name = 'queryset'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        python = Python.objects.all()
        queryset = Python 
        # category_count = queryset
        context = super().get_context_data(**kwargs)
        context['page_request_var'] = "page"
        # context['category_count'] = category_count
        context['python'] = python
        return context


class CList(ListView):
    model = C
    template_name = './courses/c.html'
    context_object_name = 'queryset'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        c = C.objects.all()
        queryset = C
        context = super().get_context_data(**kwargs)
        context['page_request_var'] = "page"
        context['c'] = c
        return context


class CppList(ListView):
    model = Cpp
    template_name = './courses/cpp.html'
    context_object_name = 'queryset'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        cpp = Cpp.objects.all()
        queryset = Cpp
        context = super().get_context_data(**kwargs)
        context['page_request_var'] = "page"
        context['cpp'] = cpp
        return context


class JavaList(ListView):
    model = Java
    template_name = './courses/java.html'
    context_object_name = 'queryset'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        java = Java.objects.all()
        queryset = Java
        context = super().get_context_data(**kwargs)
        context['page_request_var'] = "page"
        context['java'] = java
        return context


class JsList(ListView):
    model = JavaScript
    template_name = './courses/js.html'
    context_object_name = 'queryset'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        js = JavaScript.objects.all()
        queryset = JavaScript
        context = super().get_context_data(**kwargs)
        context['page_request_var'] = "page"
        context['js'] = js
        return context
