from django.urls.conf import include
from rest_framework import routers
from django.urls import path
from .import views


router = routers.SimpleRouter()
router.register('usercustomize', views.Users, basename='Users')
router.register('upload', views.DropBoxViewset,basename="upload")

urlpatterns = [
    path('api/',include(router.urls)),
    path('UserRegistration',views.UserRegistration.as_view(),name='UserRegistration'),
    path('',views.UserLogin.as_view(),name='UserLogin')
]