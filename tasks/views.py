from django.utils import timezone
from rest_framework import generics, permissions, status, filters
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Task
from .serializers import TaskSerializer


# ✅ List + Create View with Filtering, Search & Ordering
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Filter, search, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["status", "priority"]  # e.g., ?status=Pending&priority=High
    search_fields = ["title", "description"]  # e.g., ?search=report
    ordering_fields = ["due_date", "priority", "created_at"]  # e.g., ?ordering=due_date

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ✅ Retrieve + Update + Delete View
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        task = self.get_object()
        if task.status == "Completed":
            raise PermissionDenied("Completed tasks cannot be edited unless reverted to Pending.")
        serializer.save(updated_at=timezone.now())

    def delete(self, request, *args, **kwargs):
        task = self.get_object()
        if task.user != request.user:
            raise PermissionDenied("You do not have permission to delete this task.")
        return super().delete(request, *args, **kwargs)


# ✅ Mark Task as Completed
class MarkTaskCompleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            task = Task.objects.get(pk=pk, user=request.user)
        except Task.DoesNotExist:
            raise PermissionDenied("You do not have permission to modify this task.")

        if task.status == "Completed":
            return Response({"detail": "Task is already completed."}, status=status.HTTP_400_BAD_REQUEST)

        task.status = "Completed"
        task.completed_at = timezone.now()
        task.save()
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)


# ✅ Mark Task as Incomplete
class MarkTaskIncompleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            task = Task.objects.get(pk=pk, user=request.user)
        except Task.DoesNotExist:
            raise PermissionDenied("You do not have permission to modify this task.")

        if task.status == "Pending":
            return Response({"detail": "Task is already pending."}, status=status.HTTP_400_BAD_REQUEST)

        task.status = "Pending"
        task.completed_at = None
        task.save()
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
