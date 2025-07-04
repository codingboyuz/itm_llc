from django.db import models



class ProductCategory(models.TextChoices):
    DRONE = 'drone', 'Tactical Drones'
    COMMUNICATION = 'communication', 'Secure Communication Systems'
    VEHICLE = 'vehicle', 'Armored Vehicles'
    OTHER = 'other', 'Other'


# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    category = models.CharField(
        max_length=30,
        choices=ProductCategory.choices,
        default=ProductCategory.OTHER
    )
    image = models.ImageField(upload_to='media/products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
