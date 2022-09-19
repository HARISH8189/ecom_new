from django.urls import path
from . import views


urlpatterns=[
    path('sellerhome', views.seller_home),
    path('cart', views.cart),
    path('myorders', views.myorders), 
    path('addproducts', views.addproducts),
    path('change_password', views.change_password),
    path('update_stocks', views.update_stocks)
]