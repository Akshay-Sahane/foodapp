from django.urls import path
from django.views.generic import TemplateView
from .views import *


urlpatterns = [
    path("register-admin",register_admin,name="RegisterAdmin"),
    path("register-customer",register_customer,name="RegisterCustomer"),
    path("login",mylogin,name="Login"),
    path("logout",mylogout,name="Logout"),
    path("profile/<int:userId>",profile,name="profile"),
    path('review',review,name="review"),
    path('preset',TemplateView.as_view(template_name="accounts/preset.html"),name="preset"),
    path('sendotp',sendotp,name="sendotp"),
    path('otp',getotp,name="otp"),
    path('setpassword',setpassword,name="setpassword"),
]