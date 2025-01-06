from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, CustomLogoutView
from django.contrib.auth.views import LogoutView




urlpatterns=[
    path('login/', CustomLoginView.as_view(), name="login"),
    # path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),

    path('', TaskList.as_view(), name="tasklist"),
    path('task/<int:pk>/', TaskDetail.as_view(), name="task"),
    path('task-edit/<int:pk>/', TaskUpdate.as_view(), name="task-update"),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name="task-delete"),
    path('create-task/', TaskCreate.as_view(), name="task-create"),
]