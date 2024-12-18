from rest_framework.viewsets import ModelViewSet
from habits.models import Habit
from habits.paginations import CustomPagination
from habits.serializers import HabitSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from users.permissions import IsOwner


class HabitViewSet(ModelViewSet):
    """CRUD модели привычка"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination

    def get_permissions(self):
        """Ограничивает доступ"""
        if self.action in ["retrieve", "create", "update", "destroy"]:
            self.permission_classes = [IsOwner]
        return super().get_permissions()

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class PublicHabitListView(generics.ListAPIView):
    """Список публичных привычек"""
    queryset = Habit.objects.filter(is_published=True)
    serializer_class = HabitSerializer
    pagination_class = CustomPagination
