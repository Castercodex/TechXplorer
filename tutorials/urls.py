from django.urls import path
from .views import (
    home_view,
    PhpList,
    PythonList,
    CList,
    CppList,
    JavaList,
    JsList,
)

app_name = "tutorials"

urlpatterns = [
    path("", home_view, name="home"),
    path("course/php/", PhpList.as_view(), name="php"),
    path("course/python/", PythonList.as_view(), name="python"),
    path("course/c/", CList.as_view(), name="c"),
    path("course/cpp/", CppList.as_view(), name="cpp"),
    path("course/java/", JavaList.as_view(), name="java"),
    path("course/js/", JsList.as_view(), name="js"),
]
