from django.urls import path
from .views import (
    TaskListCreateView,
    TaskDetailView,
    MarkTaskCompleteView,
    MarkTaskIncompleteView,
)

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/complete/', MarkTaskCompleteView.as_view(), name='task-complete'),
    path('tasks/<int:pk>/incomplete/', MarkTaskIncompleteView.as_view(), name='task-incomplete'),
]
