from django.urls import path
from . import views


urlpatterns = [
    path('', views.guidanceDashboard, name='guidanceDashboard'),   
    path('level/', views.studentList, name='studentList'),
    path('gradeeight/', views.gradeeight, name='gradeeight'),
    path('gradenine/', views.gradenine, name='gradenine'),
    path('gradeten/', views.gradeten, name='gradeten'),


    path('studentprofile/', views.studentProfile, name='profile'),
    path('acads/', views.acads, name='acads'),


    #grade7
    path('sectionone/', views.sectionOne, name='sectionOne'),
    path('sectiontwo/', views.sectionTwo, name='sectionTwo'),
    path('sectionThree/', views.sectionThree, name='sectionThree'),
    path('sectionFour/', views.sectionFour, name='sectionFour'),
    path('sectionFive/', views.sectionFive, name='sectionFive'),


    #grade8
    path('eightsectionone/', views.eightsectionOne, name='eightsectionOne'),
    path('eightsectiontwo/', views.eightsectionTwo, name='eightsectionTwo'),
    path('eightsectionThree/', views.eightsectionThree, name='eightsectionThree'),
    path('eightsectionFour/', views.eightsectionFour, name='eightsectionFour'),
    path('eightsectionFive/', views.eightsectionFive, name='eightsectionFive'),

    #grade9
    path('ninesectionone/', views.ninesectionOne, name='ninesectionOne'),
    path('ninesectiontwo/', views.ninesectionTwo, name='ninesectionTwo'),
    path('ninesectionThree/', views.ninesectionThree, name='ninesectionThree'),
    path('ninesectionFour/', views.ninesectionFour, name='ninesectionFour'),
    path('ninesectionFive/', views.ninesectionFive, name='ninesectionFive'),
    
    #grade10
    path('tensectionone/', views.tensectionOne, name='tensectionOne'),
    path('tensectiontwo/', views.tensectionTwo, name='tensectionTwo'),
    path('tensectionThree/', views.tensectionThree, name='tensectionThree'),
    path('tensectionFour/', views.tensectionFour, name='tensectionFour'),
    path('tensectionFive/', views.tensectionFive, name='tensectionFive'),
    
]