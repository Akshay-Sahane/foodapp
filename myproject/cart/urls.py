from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('addtocart/<int:foodId>',addtocart,name="addtocart"),
    path('viewcart',viewcart,name="viewcart"),
    path('removeitem/<int:pk>',removeitem,name="removeitem"),
    path('updatecart',updatecart,name="updatecart"),
    path('order',order,name="order"),
]