from django.urls import path
from user_profile.api.views import (PilotInformationDetailAPIView, PilotInformationListAPIView)

urlpatterns = [
    path("pilot/", PilotInformationListAPIView.as_view(), name="pilot-list"),
    path("pilot/<int:pk>", PilotInformationDetailAPIView.as_view(), name="pilot-detail")

]