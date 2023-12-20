from django.shortcuts import render
from .serializers import ProductslistSerializers
from rest_framework.generics import ListCreateAPIView
from .models import Productslist

class apiView(ListCreateAPIView):
    queryset=Productslist.objects.all().order_by('-review')
    serializer_class = ProductslistSerializers

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        producttype = self.request.query_params.get('producttype', None)
        price = self.request.query_params.get('price', None)
        review = self.request.query_params.get('review', None)
        manufacturer = self.request.query_params.get('manufacturer', None)

        queryset = super().get_queryset()

        if name:
            queryset = queryset.filter(name__contains=name)
        if producttype:
            queryset = queryset.filter(producttype__iexact=producttype)
        if manufacturer:
            queryset = queryset.filter(manufacturer__contains=manufacturer)
        if price:
            queryset = queryset.filter(price__lte=price)
        if review:
            queryset = queryset.filter(review__gte=review)
            
        return queryset