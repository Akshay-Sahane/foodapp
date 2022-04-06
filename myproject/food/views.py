from django.shortcuts import redirect, render

# Create your views here.


from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Food
from .forms import FoodForm
from django.urls import reverse_lazy

# CreateView is used for creation,updation,deletion
class FoodCreateView(SuccessMessageMixin,CreateView):
    model = Food
    form_class=FoodForm
    template_name = "food/foodform.html"
    success_message="food is added successfully..."
    success_url=reverse_lazy('foodlist')


from django.views.generic.list import ListView

class FoodListView(ListView):
    model = Food
    template_name = "food/foodlist.html"


from django.views.generic.edit import UpdateView

class FoodUpdateView(SuccessMessageMixin,UpdateView):
    model = Food
    form_class=FoodForm
    template_name ="food/foodform.html"
    success_message="Food Is Updated Successfully..."
    success_url=reverse_lazy("foodlist")


from django.views.generic.edit import DeleteView
class FoodDeleteView(SuccessMessageMixin,DeleteView):
    model = Food
    template_name = "food/delete_confirm.html"
    success_message="Food is Deleted Successfully..."
    success_url = reverse_lazy("foodlist")


def foodsortname(req):
    flist=Food.objects.order_by('foodName')
    context={'object_list':flist}
    return render(req,"food/foodlist.html",context)

def foodsortpriceasc(req):
    flist=Food.objects.order_by('foodPrice')
    context={'object_list':flist}
    return render(req,"food/foodlist.html",context)

def foodsortpricedesc(req):
    flist=Food.objects.order_by('-foodPrice')
    context={'object_list':flist}
    return render(req,"food/foodlist.html",context)


def searchfood(req):
    q=req.GET['q']
    l=q.lower()
    flist=Food.objects.filter(foodName=l)
    context={'object_list':flist}
    return render(req,"food/foodlist.html",context)