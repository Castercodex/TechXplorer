from django.urls import path
from .views import c_course

app_name = 'tutorials'

urlpatterns = [
    path('', c_course, name='home')
]
