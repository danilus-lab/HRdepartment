from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('dismiss', views.dismiss, name='dismiss'),
    path('workers', views.workers, name='workers'),
    path('staff_list', views.staff_list, name='staff_list')
]
