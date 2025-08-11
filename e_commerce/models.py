from django.db import models

# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    seller = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    product_dimensions = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name