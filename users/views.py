from users.models import User
from users.serializers import UserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="Контроллер для получения списка всех пользователей"
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="Контроллер для получения пользователя"
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="Контроллер для создания пользователя"
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="Контроллер для обновления пользователя"
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_description="Контроллер для удаления пользователя"
))
class UserCreateAPIView(CreateAPIView):
    """CRUD для регистрации пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
