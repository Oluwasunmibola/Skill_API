from rest_framework.routers import DefaultRouter
from .views import SkillViewSet, ProgressViewSet, register_user, login_user
from django.urls import path, include

router = DefaultRouter()
router.register(r'skills', SkillViewSet)
router.register(r'progress', ProgressViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user),
    path('logIn/', login_user)
]