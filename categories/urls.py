from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/homepage
    path('', views.index, name="categories-index"),

    ]

