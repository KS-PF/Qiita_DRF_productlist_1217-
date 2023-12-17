from rest_framework import serializers
from .models import Productslist

class ProductslistSerializers(serializers.ModelSerializer):
    class Meta:
        model= Productslist
        fields=["id","name","producttype","description","price","review","manufacturer"]