from django.urls import path
from todo import views


urlpatterns = [
    path('createtodo', views.createtodo, name='createtodo'),
    path('alltodo', views.alltodo, name='alltodo'),
    path('deletetodo/<int:id>', views.deletetodo, name='deletdeletetodo'),
    path('tododetails/<int:id>', views.tododetails, name='tododetails'),
    path('todoedit/<int:id>', views.todoedit, name='todoedit'),
    path('index', views.index, name='index'),
    
    
]
