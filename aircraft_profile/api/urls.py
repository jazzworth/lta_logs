from django.urls import path
from aircraft_profile.api.views import (AircraftDetailAPIView, AircraftListAPIView)

urlpatterns = [
    path("aircraft/", AircraftListAPIView.as_view(), name="aircraft-list"),
    path("aircraft/<int:pk>", AircraftDetailAPIView.as_view(), name="aircraft-detail")

]
