from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from .views import *

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('problemes/<str:matricule>', ProblemeVoitureViews.as_view()),
    path('voitures/', VoitureViews.as_view())
]