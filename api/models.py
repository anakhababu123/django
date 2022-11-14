from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True,blank=True)



    def __str__(self):
        return self.name


class Reviews(models.Model):
    comment=models.CharField(max_length=200)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MaxValueValidator(5),MinValueValidator(1),])


# localhost:8000/products/2/review/

class Carts(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    
