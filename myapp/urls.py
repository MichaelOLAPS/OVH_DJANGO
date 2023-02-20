from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name="index"),
    path('formulaire',views.get_name,name="form"),
]
