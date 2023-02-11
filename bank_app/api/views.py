from django.shortcuts import render
from ..models import *
from .serializers import *
from .pagination import *

from rest_framework import generics, mixins
from rest_framework import filters

# Create your views here.

class BankList(generics.ListAPIView, generics.GenericAPIView):
    """Listing bank objects"""
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    pagination_class = BankListPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'id']


class BranchList(generics.ListAPIView, generics.GenericAPIView):
    """Listing branch objects"""
    serializer_class = BranchSerializer
    pagination_class = BranchListPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['ifsc', 'bank__name', 'city', 'district', 'address']

    def get_queryset(self):
        """get branch list of specific bank"""
        id = self.kwargs.get('pk')
        return Branche.objects.filter(bank_id=id)

