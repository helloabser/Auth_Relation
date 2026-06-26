from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):

    def __str__(self):
        return self.username


class ProductModel(models.Model):
    name = models.CharField(max_length=250, null=True)
    price = models.IntegerField(null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='media/products', null=True)

    def __str__(self):
        return self.name
    
class OrderModel(models.Model):
    STATUS =[
        ('pending','Pending'),
        ('in-Progress','In-Progress'),
        ('deliverd','Deliverd'),
    ]

    user = models.ForeignKey(UserModel,on_delete=models.CASCADE , null=True)
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE, null=True)
    status = models.CharField(choices=STATUS, null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f" Product :{self.product }"