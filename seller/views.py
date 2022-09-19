from django.shortcuts import render

# Create your views here.
def seller_home(request):
    return render(request, 'sellertemplates/sellerhome.html')

def cart(request):
    return render(request, 'sellertemplates/cart.html')    

def myorders(request):  
    return render(request, 'sellertemplates/myorders.html')   

def addproducts(request):
    return render(request, 'sellertemplates/addproducts.html')  

def change_password(request):
    return render(request, 'sellertemplates/change_password.html')   

def update_stocks(request):
    return render(request, 'sellertemplates/update_stocks.html')       