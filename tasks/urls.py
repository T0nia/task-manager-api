from django.urls import path
from .views import (
    TaskListCreateView,
    TaskDetailView,
    MarkTaskCompleteView,
    MarkTaskIncompleteView,
)

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='task-list-create'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('<int:pk>/complete/', MarkTaskCompleteView.as_view(), name='task-complete'),
    path('<int:pk>/incomplete/', MarkTaskIncompleteView.as_view(), name='task-incomplete'),
]
