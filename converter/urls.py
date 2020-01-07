from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('About/',views.about, name='about'),
    path('Create/',views.create, name='create'),
]
