from users.models import User
from users.serializers import UserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny


class UserCreateAPIView(CreateAPIView):
    """CRUD для регистрации пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()