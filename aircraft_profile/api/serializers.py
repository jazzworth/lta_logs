from rest_framework import serializers
from aircraft_profile.models import Balloon


class AircraftProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Balloon
        fields = "__all__"
        


    