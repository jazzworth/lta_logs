from rest_framework import serializers

from user_profile.models import PilotInformation


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = PilotInformation
        fields = "__all__"