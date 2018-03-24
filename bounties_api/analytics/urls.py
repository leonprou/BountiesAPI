from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from analytics import views

router = DefaultRouter()

router.register(r'analytics', views.BountyStatsViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
