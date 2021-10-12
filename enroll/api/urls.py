from django.urls import path,include
from rest_framework import urlpatterns
from enroll.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('crud', views.userview, basename='user')

urlpatterns = [
    path('', include(router.urls))
]
