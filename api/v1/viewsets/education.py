from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins
from api.v1.serializers.education import EducationSerializers


class EducationViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = EducationSerializers
    permission_classes = [IsAuthenticated]

