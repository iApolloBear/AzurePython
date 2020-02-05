from rest_framework import serializers
from . import models


class PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Promo
        fields = '__all__'
