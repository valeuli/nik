from rest_framework import viewsets, mixins
from api.v1.serializers.user import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User


class RegisterViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
	permission_classes = []
	serializer_class = RegisterSerializer


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
	permission_classes = []
	serializer_class = UserSerializer

	def get_queryset(self):
		return User.objects.all()
