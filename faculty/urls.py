from django.urls import path
from . import views

urlpatterns = [
    path('', views.faculty_dashboard, name='faculty_dashboard'),
    path('list/', views.master_list, name="master_list"),
    path('record/', views.acads_record, name="acads_record"),
    path('account/', views.account_setting, name='account_setting'),
    path('setting/', views.settings, name='settings')
]