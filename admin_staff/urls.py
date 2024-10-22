from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('annoucement/<int:id>', views.annoucement, name="annoucement" ),
    path('update_announcement/<int:id>', views.update_announcement, name='update_announcement'),
    
    path('class/', views.classes, name='classes'),

    path('student/', views.student_list, name='student_list'),
    path('student_profile/<int:pk>', views.student_profile, name='student_profile'),   
    
    path('faculty/', views.faculty_list, name='faculty_list'),

]