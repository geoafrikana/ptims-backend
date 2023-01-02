from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('buildings', views.BuildingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
