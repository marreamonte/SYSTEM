from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('edit<int:id>', views.edit_annoucement, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    

    path('class/', views.classes, name='classes'),

    path('student/', views.student_list, name='student_list'),
    path('student_profile/<int:pk>', views.student_profile, name='student_profile'),   
    
    path('faculty/', views.faculty_list, name='faculty_list'),

]