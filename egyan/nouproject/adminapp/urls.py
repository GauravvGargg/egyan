from django.urls import path
from . import views

urlpatterns=[
    path('',views.adminhome,name='adminhome'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('managestudymaterial/', views.managestudymaterial, name='managestudymaterial'),
    path('managestudent/', views.managestudent, name='managestudent'),
    path('managefeedback/', views.managefeedback, name='managefeedback'),
    path('manageenquiry/', views.manageenquiry, name='manageenquiry'),
    path('managecomplaint/', views.managecomplaint, name='managecomplaint'),
    path('deleteenq/<id>',views.deleteenq,name='deleteenq'),
    path('deletefeed/<id>',views.deletefeed,name='deletefeed'),
    path('deletecomp/<id>',views.deletecomp,name='deletecomp'),
    path('viewmaterial/',views.viewmaterial,name='viewmaterial'),
    path('deletesmat/<mid>',views.deletesmat,name='deletesmat'),


]