from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from store.models import Customers, Messages, UserAccount, Product, Page
from cpanel.forms import CustomersForm, ProductForm, EditproductForm, Signinform
from django.contrib.auth.models import User
from cpanel.resize import shrink
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json
# Create your views here.
webaddress = ["http://127.0.0.1:8000"]

@login_required
def dashboard(request):
    users = (User.objects.count())
    all_accounts = UserAccount.objects.all()
    products = Product.objects.order_by('-added')[:6]
    count = Product.objects.count()
    messages = Messages.objects.all()
    page = Page.objects.get(id = 1)
    print(messages)
    context = {"webaddress":webaddress[0],"count":count, "products":(products), "messages":(messages), "all_accounts":all_accounts,"page": page, "users":users}
    return render(request, 'admin/dashboard.html', context)

@login_required
def tables(request):
    form = ProductForm()
    products = Product.objects.order_by("-id")
    context = {"webaddress":webaddress[0], "form": form, "products":products}
    return render(request, 'admin/table.html', context)

@login_required
def product(request, id):
    form = ProductForm()
    products = Product.objects.get(id = id)
    context = {"webaddress":webaddress[0], "form": form, "products":products}
    return render(request, 'admin/edit.html', context)

@login_required
def add_product(request):

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            cleaned = (form.cleaned_data)
            name = cleaned['name']
            price = cleaned['price']
            incoming_prod = Product.objects.filter(name = "name")

            if incoming_prod.exists():
                print('product exists')
            
            if request.FILES['image']:
                image = request.FILES['image']
                new_product = Product(name = name, price = price, image = image)
                new_product.save()
                print(new_product.image.path)
                shrink(new_product.image.path)
            else:
                try:
                    if request.FILES['image']:
                        image = request.FILES['image']
                        shrink(image)
                        new_product = Product(name = name, price = price, image = image)
                        new_product.save()
                except:
                    
                    new_product = Product(name = name, price = price)
                    new_product.save()
    context = {"webaddress":webaddress[0]}
    return tables(request)

@login_required
def edit_product(request, id):
    
    if request.method == "POST":

        form = EditproductForm(request.POST)
        if form.is_valid():
            print(form)
            print("valid ============")
            cleaned = (form.cleaned_data)
            incoming_prod = Product.objects.get(id = id)
            name = cleaned['new_name'] 
            price = cleaned['price']
            
            try:
                if request.FILES['image']:
                    incoming_prod.image = request.FILES['image']
                    incoming_prod.name = name 
                    incoming_prod.price = price
                    incoming_prod.save()
            except:
                incoming_prod.name = name 
                incoming_prod.price = price
                incoming_prod.save()
                    
    context = {"webaddress":webaddress[0]}
    return product(request, id)

@login_required
def delete_product(request, id):
    
    if request.method == "POST":
        print(request.POST['product'])
        incoming_prod = Product.objects.get(id = id)
        incoming_prod.delete()
        
                    
    context = {"webaddress":webaddress[0]}
    return tables(request)

@login_required
def mail(request):
    if request.method == "POST":
        name = (request.POST["name"])
        price = request.POST["price"]
        incoming_prod = Product.objects.filter(name = "name")

        if incoming_prod.exists():
            print('email exists')
        else:
            new_product = Product(name = name, price = price)
            new_product.save()

    context = {"webaddress":webaddress[0]}
    return HttpResponse({"webaddress":webaddress[0]})

@login_required
def notifications(request):
    
    messages = Messages.objects.order_by('-added')
    
    context = {"webaddress":webaddress[0], "messages":(messages)}
    

    return render(request, 'admin/notifications.html', context)

def signin(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)

            res = json.dumps('true')
            return HttpResponse(res)
        else:
            res = json.dumps('Username/Password combination might be wrong')
            return HttpResponse(res)
    
    else:
        return render(request, 'admin/login.html', {"webaddress":webaddress[0], "error": "Username or password incorrect"})

def settings(request):
    page = Page.objects.get(id = 1)
    return render(request, 'admin/settings.html', {"webaddress":webaddress[0], "page":page, "error": "Username or password incorrect"})

@login_required
def set_mail (request):
    if request.method == "POST":
        print(request.POST)
        page = Page.objects.get(id = 1)
        email = request.POST['email']
        
        if email is not None:
            page.email = email
            page.save()

            res = json.dumps('Successfully Changed Email')
            return HttpResponse(res)
        else:
            res = json.dumps('failed')
            return HttpResponse(res)

def set_pass (request):
    if request.method == "POST":
        print(request.POST["old"])
        old = request.POST["old"]
        password = request.POST['newpass']
        user = User.objects.get(username="moremi")
        pass_check = authenticate(username = user.username, password = old)
        print(pass_check)
        if pass_check is not None:
            user.set_password(password)
            user.save()
            pass
            res = json.dumps('Successfully Changed Pass')
            return HttpResponse(res)
        else:
            res = json.dumps('error')
            return HttpResponse(res)