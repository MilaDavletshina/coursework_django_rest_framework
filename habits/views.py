from rest_framework.viewsets import ModelViewSet
from habits.models import Habit
from habits.serializers import HabitSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwner


class HabitViewSet(ModelViewSet):
    """CRUD модели привычка"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        """Ограничивает доступ модератору"""
        if self.action != "create":
            self.permission_classes = [IsOwner]
        return super().get_permissions()

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()