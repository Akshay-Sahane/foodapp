
from django.urls import path
from .views import *

urlpatterns = [
    path('order',order,name="order"),
    path('payment/<str:amt>',payment,name="payment"),
]