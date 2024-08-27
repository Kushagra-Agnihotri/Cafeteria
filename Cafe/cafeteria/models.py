from django.db import models

class Dish(models.Model):
    
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(max_length= 500,default= "Delicious Delight!")
    image_locat = models.CharField(max_length= 50,default="images/dish1.jpeg")

    def __str__(self):
        return self.name

class CartItem(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.dish.name} - {self.quantity}'
