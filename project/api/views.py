from rest_framework import serializers, generics
from .models import cars
from .serializer import carsSerializer



  #########  generics views  ########

class carsList(generics.ListCreateAPIView):
    queryset = cars.objects.all()
    serializer_class = carsSerializer

class carsdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = cars.objects.all()
    serializer_class = carsSerializer
    
    


