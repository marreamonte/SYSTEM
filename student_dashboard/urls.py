from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name="profile"),
    path('academic/', views.academic, name="academic"),
    path('bill/', views.bill, name="bill")
]