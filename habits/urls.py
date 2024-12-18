from django.urls import path
from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import HabitViewSet, PublicHabitListView, HabitsListViewSet

app_name = HabitsConfig

router = DefaultRouter()
router.register(r'habit', HabitViewSet, basename='habit')

urlpatterns = [
    path("habits/public/", PublicHabitListView.as_view(), name="public-habit-list"),
    path("habits-list/", HabitsListViewSet.as_view(), name="habits-list"),
] + router.urls


