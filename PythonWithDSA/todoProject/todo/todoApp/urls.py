from django.urls import path
from . import views


urlpatterns = [
    path('', views.addTask, name='main'),
    path('statusupdate/<id>', views.updateStatus, name='status'),
    path('delete/<id>', views.delete, name='delete'),
]



# www.example.com/u