from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        f_name = request.POST.get('f_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        user_exist = UserModel.objects.filter(username=username).exists()
        email_exist = UserModel.objects.filter(email=email).exists()

        if user_exist or email_exist:
            return HttpResponse('Username and email already Exist')
        else:
            if password == confirm_password:

                UserModel.objects.create_user(
                    username = username,
                    email = email,
                    first_name = f_name,
                    password = password
                )
                return redirect('login')
    return render(request, 'auth/register.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')        
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('dashboard')

    return render(request, 'auth/login.html')

def dashboardPage(request):

    productData = ProductModel.objects.all()
    context = {
        'product_data':productData
    }

    return render(request,'pages/dashboard.html',context)

def addProductPage(request):
    if request.method == "POST":
        name = request.POST.get('p_name')
        price = request.POST.get('p_price')
        description = request.POST.get('p_description')
        image = request.FILES.get('p_image')

        ProductModel.objects.create(
            name = name,
            price = price,
            description = description,
            image = image,
        )
        return redirect('dashboard')

    return render(request,'pages/addProduct.html')

def orderPage(request,id):
    get_product = ProductModel.objects.get(id=id)

    if get_product:
        OrderModel.objects.create(
            product = get_product,
            user = request.user ,
            status = 'Pending',
        )
        return redirect('orderList')
    
def orderListPage(request):
    
    context = {
        'orderData': OrderModel.objects.all()
    }
    return render(request, 'pages/orderList.html', context)
    