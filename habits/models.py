from django.db import models
from users.models import User
from datetime import timedelta


NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    """Модель привычки."""

    PERIODICITY_CHOICES = [
        ("every day", "каждый день"),
        ("once a week", "раз в неделю"),
        ("twice a week", "дважды в неделю"),
        ("three times a week", "трижды в неделю"),
        ("four times a week", "четыре раза в неделю"),
        ("five times a week", "пять раз в неделю"),
        ("six times a week", "шесть раз в неделю"),
    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Автор привычки",
        help_text="Укажите автора привычки",
        related_name="users_habits",
        **NULLABLE
    )
    place = models.CharField(
        max_length=255,
        verbose_name="Место выполнения привычки",
        **NULLABLE
    )
    start_time = models.DateTimeField(
        verbose_name="Время старта",
        help_text="Выберете время когда необходимо выполнять привычку",
        **NULLABLE
    )
    action = models.CharField(
        max_length=300,
        verbose_name="Действие привычки",
        help_text="Укажите действие привычки",
        **NULLABLE
    )
    is_pleasant = models.BooleanField(
        default=False,
        verbose_name="Признак приятной привычки",
        help_text="Привычка является приятной",
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Связанная привычка",
        related_name="related_habits",
        **NULLABLE
    )
    periodicity = models.CharField(
        max_length=25,
        choices=PERIODICITY_CHOICES,
        verbose_name="Переодичность выполнения привычки",
        help_text="Укажите переодичность выполнения привычки",
        default="every day",
    )
    remuneration = models.CharField(
        verbose_name="Вознаграждение после выполнения привычки",
        **NULLABLE
    )
    execution_time = models.DurationField(
        default=timedelta(seconds=120),
        verbose_name="Время выполнения привычки",
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Публикация в общем доступе",
        help_text="Опубликовать для общего доступа",
    )
