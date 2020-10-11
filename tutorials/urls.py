from django.urls import path
from .views import  home_view, trial

app_name = 'tutorials'

urlpatterns = [
    path('', home_view, name='home'),
    path('course/<slug>', trial, name="course")

]
