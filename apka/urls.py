from django.urls import path, include
from rest_framework import routers
from .views import MovieViewSet, RatingViewSet, UserViewSet, ActorsViewSet, DirectorsViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('movies', MovieViewSet)
router.register('ratings', RatingViewSet)
router.register('actors', ActorsViewSet)
router.register('directors', DirectorsViewSet)

urlpatterns = [
    path('', include(router.urls))
]