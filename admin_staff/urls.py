from django.urls import path
from . import views

urlpatterns = [
    #admin board
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.admin_dashboard, name='home'),
    path('edit<int:id>', views.edit_annoucement, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    path('class/', views.classes, name='classes'),
    path('student/', views.student_list, name='student_list'),
    path('student_profile/<int:pk>', views.student_profile, name='student_profile'),   
    path('faculty/', views.faculty_list, name='faculty_list'),
    path('profile/<int:pk>', views.faculty_profile, name='faculty_profile'),

    #student board
    path('student', views.student_dashboard, name='student')
]