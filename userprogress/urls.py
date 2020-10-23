from django.urls import path
from .views import dashboard, add_to_enrolled

app_name = 'user_progress'

urlpatterns = [
    path('dashboard/', dashboard, name='Dashboard'),
    path('add_to_enrolled/<slug>/', add_to_enrolled, name="add-to-enrolled")

]
