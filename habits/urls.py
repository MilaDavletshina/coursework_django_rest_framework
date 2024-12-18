from django.urls import path
from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import HabitViewSet, PublicHabitListView

app_name = HabitsConfig

router = DefaultRouter()
router.register(r'habit', HabitViewSet, basename='habit')

urlpatterns = [
    path('habits/public/', PublicHabitListView.as_view(), name='public-habit-list')
] + router.urls


