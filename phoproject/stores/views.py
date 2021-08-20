from django.shortcuts import render
from rest_framework import generics
from .serializers import PhoPlaceDetailSerializer, PhoPlaceListSerializer
from .models import PhoPlace
# Create your views here.


class PhoPlaceListAPIView(generics.ListAPIView):
    queryset = PhoPlace.objects.all()
    print(queryset)
    serializer_class = PhoPlaceListSerializer


class PhoPlaceRetrieveView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = PhoPlace.objects.all()
    serializer_class = PhoPlaceDetailSerializer


class PhoPlaceCreateAPIView(generics.CreateAPIView):
    queryset = PhoPlace.objects.all()
    serializer_class = PhoPlaceDetailSerializer

class PhoPlaceRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    queryset = PhoPlace.objects.all()
    serializer_class = PhoPlaceDetailSerializer

class PhoPlaceDeleteView(generics.DestroyAPIView):
    lookup_field = "id"
    queryset = PhoPlace.objects.all()