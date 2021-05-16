from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=10000)
    price = models.DecimalField(max_digits=10000,decimal_places=2)
    description = models.TextField()
    short = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name
