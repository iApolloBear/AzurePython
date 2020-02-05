from django.shortcuts import render
from rest_framework import generics
from .serializers import PromoSerializer
from .models import Promo


# Create your views here.
class PromoList(generics.ListCreateAPIView):
    queryset = Promo.objects.all()
    serializer_class = PromoSerializer


class PromoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promo.objects.all()
    serializer_class = PromoSerializer
