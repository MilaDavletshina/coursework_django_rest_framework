from rest_framework.routers import SimpleRouter

from habits.apps import HabitsConfig
from habits.views import HabitViewSet

app_name = HabitsConfig

router = SimpleRouter()
router.register("", HabitViewSet)

urlpatterns = []

urlpatterns += router.urls
