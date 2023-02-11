from rest_framework import serializers

from ..models import *



class BankSerializer(serializers.ModelSerializer):
    """Serializes a bank object"""
    class Meta:
        model = Bank
        fields = '__all__'



class BranchSerializer(serializers.ModelSerializer):
    """Serializes a branch object"""
    bank = serializers.StringRelatedField()
    class Meta:
        model = Branche
        fields = '__all__'
