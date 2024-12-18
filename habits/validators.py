# from datetime import timedelta
#
# from rest_framework.serializers import ValidationError
#
#
# class RelatedOrIsPleasantValidator:
#     """Исключение одновременного выбора связанной привычки и указания вознаграждения"""
#     def __init__(self, related_habit):
#         self.related_habit = related_habit
#
#     def __call__(self, value):
#         habit = value.get(self.related_habit)
#         if habit:
#             if not habit.is_pleasant:
#                 raise ValidationError("Не может быть заполнено одновременно и поле вознаграждения, и поле связанной привычки. Можно заполнить только одно из двух полей.")
#
#
# class TimeLimiter:
#     def __init__(self, execution_time):
#         self.execution_time = execution_time
#
#     def __call__(self, value):
#         time = value.get(self.execution_time)
#         if time > timedelta(seconds=120):
#             raise ValidationError("Время выполнения должно быть не больше 120 секунд")