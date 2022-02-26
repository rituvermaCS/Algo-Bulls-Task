from django.urls import path
from . import views

urlpatterns = [
    path('api/read-all/', views.taskList, name="task-list"),
    path('api/read-one/<str:pk>/', views.taskDetail, name="task-Detail"),
    path('api/update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('api/create/', views.taskCreate, name="task-Create"),
    path('api/delete/<str:pk>/', views.taskDelete, name="task-delete"),
]
