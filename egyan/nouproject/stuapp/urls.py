from django.urls import path
from . import views

urlpatterns=[
    path('',views.stuhome,name='stuhome'),
    path('logout/',views.logout,name='logout'),
    path('assignments/', views.assignments, name='assignments'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('response/', views.response, name='response'),
    path('studymaterial/', views.studymaterial, name='studymaterial'),
]