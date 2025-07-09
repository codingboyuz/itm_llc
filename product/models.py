


from django.db import models
from django.utils.translation import gettext_lazy as _



class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    verbose_name = models.CharField(max_length=255, verbose_name=_("Display Name"))

    def __str__(self):
        return self.verbose_name

class ProductModel(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(ProductModel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/products/')

    def __str__(self):
        return f"Image for {self.product.name}"


class ProductField(models.Model):
    product = models.ForeignKey(ProductModel, related_name='fields', on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.key}: {self.value} ({self.product.name})"
