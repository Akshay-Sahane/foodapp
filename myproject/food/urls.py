from django.urls import path
from django.views.generic.base import TemplateView
from .views  import *

urlpatterns = [
    path('',TemplateView.as_view(template_name="food/index.html"),name="Home"),
    path('create-food/',FoodCreateView.as_view(),name="addfood"),
    path('foodlist/',FoodListView.as_view(),name="foodlist"),
    path('update-food/<int:pk>',FoodUpdateView.as_view(),name="update-food"),
    path('delete-food/<int:pk>',FoodDeleteView.as_view(),name='delete-food'),
    path('foodsortname',foodsortname,name="foodsortname"),
    path('foodsortpriceasc',foodsortpriceasc,name="foodsortpriceasc"),
    path('foodsortpricedesc',foodsortpricedesc,name="foodsortpricedesc"),
    path('searchfood',searchfood,name="searchfood"),
]