from rest_framework import serializers
from . import models


class PeronsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ('id', 'face')


class GetIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ('face',)
