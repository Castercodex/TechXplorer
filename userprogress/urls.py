from django.urls import path
from .views import dashboard

app_name = 'user_progress'

urlpatterns = [
    path('dashboard/', dashboard, name='Dashboard'),


]
