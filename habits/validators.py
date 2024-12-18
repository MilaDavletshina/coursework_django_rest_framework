from datetime import timedelta
from rest_framework.serializers import ValidationError


class FillingTheFieldValidator:
    """Проверка наличия у приятной привычки связанной привычки или вознаграждения"""

    def __init__(self, is_pleasant, related_habit, remuneration):
        self.is_pleasant = is_pleasant
        self.related_habit = related_habit
        self.remuneration = remuneration

    def __call__(self, value):
        is_pleasant_field = value.get(self.is_pleasant)
        related_habit_field = value.get(self.related_habit)
        remuneration_field = value.get(self.remuneration)

        if (is_pleasant_field and related_habit_field) or (is_pleasant_field and remuneration_field):
            raise ValidationError("У приятной привычки не может быть связанной привычки или вознаграждения")


class RelatedOrIsPleasantValidator:
    """Проверка связанной привычки на признак приятной привычки"""
    def __init__(self, related_habit):
        self.related_habit = related_habit

    def __call__(self, value):
        habit = value.get(self.related_habit)

        if habit:
            if not habit.is_pleasant:
                raise ValidationError("Связанная привычка должна иметь признак приятной привычки.")


class TimeLimiter:

    def __init__(self, execution_time):
        self.execution_time = execution_time

    def __call__(self, value):
        time = value.get(self.execution_time)
        if time > timedelta(seconds=120):
            raise ValidationError("Время выполнения должно быть не больше 120 секунд")