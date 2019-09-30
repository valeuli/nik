from django.urls import include, path
from rest_framework import routers
from api.v1.viewsets.education import EducationViewSet


router = routers.SimpleRouter()
router.register(r'education', EducationViewSet, base_name='education')

urlpatterns = [path('', include(router.urls)), ]
