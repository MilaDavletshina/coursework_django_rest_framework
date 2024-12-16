from rest_framework import serializers
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """Серилизатор модели привычка."""
    class Meta:
        model = Habit
        fields = "__all__"
