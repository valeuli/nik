from django.urls import include, path
from rest_framework import routers
from api.v1.viewsets.user import RegisterViewSet, UserViewSet

router = routers.SimpleRouter()
router.register(
		r'register', RegisterViewSet, base_name='register'
	)
router.register(
		r'userviewset', UserViewSet, base_name='userviewset'
)
urlpatterns = [
		path('', include(router.urls)),
	]
