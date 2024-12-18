from rest_framework import serializers
from habits.models import Habit
from habits.validators import RelatedOrIsPleasantValidator


class HabitSerializer(serializers.ModelSerializer):
    """Серилизатор модели привычка."""
    validators = serializers.CharField(validators=[RelatedOrIsPleasantValidator()])

    class Meta:
        model = Habit
        fields = "__all__"

