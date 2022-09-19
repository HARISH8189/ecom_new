from django.urls import path
from . import views

urlpatterns=[
    path('customer home',views.customer_home), 
    path('cart',views.customer_cart)
]