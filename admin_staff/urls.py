from django.urls import path
from . import views

urlpatterns = [
    #login Page
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    
    #admin board
    path('', views.admin_dashboard, name='home'),
    path('class/', views.classes, name='classes'),
    path('student/', views.student_list, name='student_list'),
    path('student/<int:pk>', views.student, name='studentinfo'),   
    path('faculty-list/', views.faculty_list, name='faculty_list'),
    path('profile/<int:pk>', views.faculty_profile, name='faculty_profile'),
    path('record', views.accademic_record, name='record'),

    #student board
    path('student', views.student_dashboard, name='student'),
    path('profile', views.student_profile, name='student-profile'),


    #faculty board
    path('faculty', views.faculty_dashboard, name='faculty'),
    path('advisory', views.advisory, name='advisory'),
    path('adviser', views.faculty_info, name='faculty_info'),
    path('info/<int:pk>', views.student_info, name='info'),
    
]