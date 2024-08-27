from django.urls import path,include
from homePage import views


app_name = 'homePage'

urlpatterns = [
    path('projects/', views.all_projects.as_view()),
    path('<slug:slug>/', views.project.as_view()),

    
]