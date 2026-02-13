from django.urls import path, include
from rest_framework import routers
from .views import ProfileViewSet, ProjectViewSet, ConnectionViewSet, CollaborationViewSet

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'connections', ConnectionViewSet)
router.register(r'collaborations', CollaborationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
