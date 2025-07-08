# from django.db import models
#
#
#
# class ProductCategory(models.TextChoices):
#     DRONE = 'drone', 'Tactical Drones'
#     COMMUNICATION = 'communication', 'Secure Communication Systems'
#     VEHICLE = 'vehicle', 'Armored Vehicles'
#     OTHER = 'other', 'Other'
#
#
# # Create your models here.
# class ProductModel(models.Model):
#     name = models.CharField(max_length=300)
#     description = models.TextField()
#     category = models.CharField(
#         max_length=30,
#         choices=ProductCategory.choices,
#         default=ProductCategory.OTHER
#     )
#     image = models.ImageField(upload_to='media/products/')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name


from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductCategory(models.TextChoices):
    DRONE = 'drone', _('Tactical Drones')
    COMMUNICATION = 'communication', _('Secure Communication Systems')
    VEHICLE = 'vehicle', _('Armored Vehicles')
    OTHER = 'other', _('Other')


class ProductModel(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    category = models.CharField(
        max_length=30,
        choices=ProductCategory.choices,
        default=ProductCategory.OTHER
    )
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
    value = models.TextField()

    def __str__(self):
        return f"{self.key}: {self.value} ({self.product.name})"
