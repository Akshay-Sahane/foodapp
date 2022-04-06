from email.mime import message
from django.shortcuts import redirect, render
from.models import Cart, CartItem
from food.models import Food
from django.contrib import messages

def addtocart(req,foodId):
    cart,status=Cart.objects.get_or_create(user=req.user)
    food=Food.objects.get(foodId=foodId)
    item=CartItem.objects.create(food=food)
    item.save()
    cart.itemlist.add(item)
    cart.save()
    if status:
        messages.success(req,"cart is created")
    else:
        messages.success(req,"cart is updated")
    messages.success(req,f"{food.foodName} is added into your cart")
    return redirect('viewcart')


def viewcart(req):
    cart,status=Cart.objects.get_or_create(user=req.user)
    context={'cart':cart}
    return render(req,"cart/viewcart.html",context)

def removeitem(req,pk):
    item=CartItem.objects.get(pk=pk)
    item.delete()
    messages.success(req,f"{item.food.foodName} is removed from cart")
    return redirect('viewcart')

from django.http import HttpResponse
import json
def updatecart(req):
    id=int(req.GET['id'])
    quantity=int(req.GET['quantity'])
    item=CartItem.objects.filter(pk=id)
    item.update(quantity=quantity)
    sub_total = item[0].sub_total
    cart,status=Cart.objects.get_or_create(user=req.user)
    final_total = cart.final_total
    print(item,sub_total)
    data={"sub_total":sub_total,"final_total":final_total}
    return HttpResponse(json.dumps(data),content_type="application/json")



def order(req):
    cart=Cart.objects.get(user=req.user)
    context={'cart':cart}
    return render(req,"checkout/order.html",context)