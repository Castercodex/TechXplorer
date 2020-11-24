from django.urls import path
from .views import (
    home_view,
    php_view,
    PythonDetail,
    c_view,
    cpp_view,
    java_view,
    js_view,
)

app_name = "tutorials"

urlpatterns = [
    path("", home_view, name="home"),
    path("course/php/", php_view, name="php"),
    path("course/python/<slug>", PythonDetail.as_view(), name="python"),
    path("course/c/", c_view, name="c"),
    path("course/cpp/", cpp_view, name="cpp"),
    path("course/java/", java_view, name="java"),
    path("course/js/", js_view, name="js"),
]
