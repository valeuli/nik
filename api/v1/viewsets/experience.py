from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins
from api.v1.serializers.experience import ExperienceSerializer


class ExperienceViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]

