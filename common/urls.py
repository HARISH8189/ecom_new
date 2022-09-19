from django.urls import path
from . import views


urlpatterns=[
    path('index', views.index),
    path('seller_login', views.seller_login),
    path('customer_login', views.customer_login),
    path('seller_signup', views.seller_signup),
    path('customer_signup', views.customer_signup),
    path('change_password', views.change_password),
    path('name', views.name)
]

 