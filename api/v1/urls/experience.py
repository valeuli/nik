from django.urls import include, path
from rest_framework import routers
from api.v1.view.sets.experience import ExperienceViewSet

router = routers.SimpleRouter()
router.register(r'experience', ExperienceViewSet, base_name='experience')

urlpatterns = [path('', include(router.urls)), ]
