from django.db import models

class Productslist(models.Model):
    name = models.CharField(max_length=32)
    producttype = models.CharField(max_length=32)
    description = models.CharField(max_length=64)
    price = models.IntegerField()
    review = models.IntegerField()
    manufacturer = models.CharField(max_length=32)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name=verbose_name_plural="商品一覧"
