from django.db.models import fields
from rest_framework import serializers
from .models import PhoPlace


class PhoPlaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoPlace
        fields = [
            'id',
            'pho_name',
            'city',
            'zip_code',
        ]


class PhoPlaceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoPlace
        fields = [
            'id',
            'pho_name',
            'street',
            'city',
            'state',
            'zip_code',
            'website',
            'phoneNumber',
            'description',
            'logo_image',
            'email',
        ]
