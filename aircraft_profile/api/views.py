from rest_framework.generics import get_object_or_404
from rest_framework import generics

from aircraft_profile.models import Balloon
from aircraft_profile.api.serializers import AircraftProfileSerializer


class AircraftListAPIView(generics.ListCreateAPIView):
    queryset = Balloon.objects.all()
    serializer_class = AircraftProfileSerializer

class AircraftDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Balloon.objects.all()
    serializer_class = AircraftProfileSerializer


# class AircraftListAPIView(APIView):
#     def get(self, request):
#         aircraft = Balloon.objects.all()
#         serializer = AircraftProfileSerializer(aircraft, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = AircraftProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class AircraftDetailAPIView(APIView):
#     def get_object(self, pk):
#         balloon = get_object_or_404(Balloon, pk=pk)
#         return balloon

#     def get(self, request, pk):
#         balloon = self.get_object(pk)
#         serializer = AircraftProfileSerializer(balloon, data=request.data)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         balloon = self.get_object(pk)
#         serializer = AircraftProfileSerializer(balloon, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         balloon = self.get_object(pk)
#         balloon.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)