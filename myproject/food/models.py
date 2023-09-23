from django.db import models


# Create your models here.

class Food(models.Model):
    foodId = models.AutoField(primary_key=True)
    foodName = models.CharField(max_length=100)
    foodType = models.CharField(max_length=20)
    foodPrice = models.FloatField()
    foodDescription = models.TextField()
    foodImage = models.URLField()

    def __str__(self):
        # return f"{self.foodName}-{self.foodType}"
        return f"{self.foodType}"
