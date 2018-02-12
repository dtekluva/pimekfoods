from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from store.models import Customers, Messages, Product, Page
from django.contrib.auth.models import User
from store.forms import CustomersForm
from store.sendmail import send as _sendmail
import json
# Create your views here.
webaddress = ["http://127.0.0.1:8000"]

def index(request):
    page = Page.objects.get(id = 1)
    page.hits +=1
    page.save()
    
    forms = CustomersForm()
    products        = Product.objects.order_by('-added')[:3]
    return render(request, 'store/index.html', {'forms':forms, 'products':products, 'webaddress':webaddress })

def catalog(request):
    
    products        = Product.objects.order_by('-added')
    return render(request, 'store/catalog.html', {'products':products, 'webaddress':webaddress })

def sendmail(request):
    page = Page.objects.get(id = 1)
    
    if request.method == "POST":
        name = (request.POST["name"])
        phone = request.POST["phone"]
        message = request.POST["message"]
        if len(name) > 2 and len(message)>2:
            new_text = Messages(name = name, phone = phone, message = message)
            new_text.save()
            _sendmail(name, message, phone, page.email)
            res = json.dumps('Received, You will get a call from us soon')

        else:
            res = json.dumps('Enter atleast 2 characters for name and message')

    return HttpResponse(res)

def address(request):
    addresses = Customers.objects.all()
    forms = CustomersForm()
    if address in addresses:
        print("True")
    return HttpResponse((addresses))

def all(request):

    products        = Product.objects.order_by('-added')

    all = []

    for item in products:
        all.append({
                                'name': item.name, 
                                'image' : item.image.url,
                                'price' : item.price 
                            })
    res = json.dumps(all)

    return HttpResponse(res)