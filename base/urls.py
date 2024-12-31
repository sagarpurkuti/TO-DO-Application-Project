from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete


urlpatterns=[
    path('', TaskList.as_view(), name="tasklist"),
    path('task/<int:pk>/', TaskDetail.as_view(), name="task"),
    path('task-edit/<int:pk>/', TaskUpdate.as_view(), name="task-update"),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name="task-delete"),
    path('create-task/', TaskCreate.as_view(), name="task-create"),
]