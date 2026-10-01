from django.db import models
from django.core.validators import MinValueValidator
class Product(models.Model):
 name=models.CharField(max_length=100)
 description=models.TextField()
 price=models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0.01,message="Price must be greater than zero.")])
 stock=models.IntegerField(validators=[MinValueValidator(0,message="Stock cannot be negative.")])
 class Meta: ordering=["id"]
 def __str__(self): return self.name
