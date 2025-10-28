from rest_framework import serializers
from django.utils import timezone
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user', 'completed_at', 'created_at', 'updated_at']

    def validate_due_date(self, value):
        """Ensure due date is in the future (serializer-level validation)."""
        if value < timezone.now().date():
            raise serializers.ValidationError("Due date must be in the future.")
        return value
