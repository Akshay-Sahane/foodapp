
from django.db import models

from food.models import Food 
# food having many items

class CartItem(models.Model):
    food=models.ForeignKey(Food,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.quantity} - {self.food.foodName}'

    @property
    def sub_total(self):
        return self.quantity * self.food.foodPrice
    @property
    def qty(self):
        return self.quantity

from accounts.models import MyUser
# one user have one and only one cart
# one cart having many items and one item in many carts(i.e.many to many)
#  

class Cart(models.Model):
    user=models.OneToOneField(MyUser,on_delete=models.CASCADE)
    itemlist=models.ManyToManyField(CartItem)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.user.first_Name}-{self.itemlist.all()}'

    @property
    def final_total(self):
        sum=0
        for item in self.itemlist.all():
            sum  = sum + (item.sub_total)
        return sum