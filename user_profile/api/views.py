from rest_framework import generics

from user_profile.api.serializers import UserProfileSerializer
from user_profile.models import PilotInformation

class PilotInformationListAPIView(generics.ListCreateAPIView):
    queryset = PilotInformation.objects.all()
    serializer_class = UserProfileSerializer


class PilotInformationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PilotInformation.objects.all()
    serializer_class = UserProfileSerializer