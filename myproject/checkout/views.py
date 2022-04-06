from django.shortcuts import redirect, render


from food.models import Food
from accounts.models import MyUser
from cart.models import CartItem,Cart
from .models import Orders

from django.http import HttpResponse
# Create your views here.

def order(req,cart,finaltotal):
    qty=cart
    context={'qty':qty,'finaltotal':finaltotal}
    return render(req,"checkout/order.html",context)

import razorpay
def payment(req,amt):
    amount=int(float(amt))*100
    client = razorpay.Client(auth=("rzp_test_7LAVaPPvvZehqa","jxfMQAqMNFyJIpSjoZXesmS7"))
    data = { "amount":amount,"currency":"INR","receipt":"order_rcptid_11" }
    payment = client.order.create(data=data)
    userid=req.user.userId
    getuser=MyUser.objects.get(userId=userid)
    uname=getuser.first_Name
    umobile=getuser.mobile_Number
    payment['username']=uname
    payment['usermobile']=umobile
    return render(req,'checkout/payment.html',payment)
'''
{'id': 'order_J83HgeFoJqvHgS', 'entity': 'order', 'amount': 2400, 'amount_paid': 0, 'amount_due': 2400, 'currency': 'INR', 'receipt': 'order_rcptid_11', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1647497334}
'''