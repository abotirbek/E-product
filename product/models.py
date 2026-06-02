from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField()
    price=models.IntegerField()
    quantity=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f"{self.title} | {self.price} | {self.quantity}"
                f"{self.created_at} {self.updated_at}"
                f"{self.description}")