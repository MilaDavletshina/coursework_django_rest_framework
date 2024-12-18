from rest_framework import serializers
from habits.models import Habit
from habits.validators import FillingTheFieldValidator, RelatedOrIsPleasantValidator


class HabitSerializer(serializers.ModelSerializer):
    """Серилизатор модели привычка."""

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            FillingTheFieldValidator(
                "remuneration",
                "related_habit",
                "is_pleasant"
            ),
            RelatedOrIsPleasantValidator("related_habit"),
        ]
