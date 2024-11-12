from django.urls import path
from . import views

urlpatterns = [
    #login Page
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    
    #admin board
    path('', views.admin_dashboard, name='home'),
    path('edit<int:id>', views.edit_annoucement, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    path('class/', views.classes, name='classes'),
    path('student/', views.student_list, name='student_list'),
    path('student/<int:pk>', views.student, name='student'),   
    path('faculty-list/', views.faculty_list, name='faculty_list'),
    path('profile/<int:pk>', views.faculty_profile, name='faculty_profile'),
    path('record', views.student_record, name='record'),

    #student board
    path('student', views.student_dashboard, name='student'),
    path('profile', views.student_profile, name='student-profile'),
    path('setting', views.setting, name='setting'),


    #faculty board
    path('faculty', views.faculty, name='faculty'),
    path('masterlist', views.faculty_student, name='faculty_student'),
    
]