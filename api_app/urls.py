from django.urls import path
from . import views 

urlpatterns= [
    # path('studentapi/', views.studentapi,name ='studentapi'),
    # path('studentapi/<int:pk>',views.studentapi,name ='studentapi'),
    
    # For Class Based View ----->
    path('studentapi/', views.StudentAPI.as_view()),
    path('studentapi/<int:pk>/',views.StudentAPI.as_view()),
]