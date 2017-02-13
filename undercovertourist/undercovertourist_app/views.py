from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.utils.html import format_html
import requests
from django.core.urlresolvers import reverse
import json

from forms import PurchaseForm
from models import Customer_purchasedata
from utils import  *
# Create your views here.
headers = {'X-Auth': '{lalasa}.{ari}'}

def index(request):
    '''
    Displays list of products along with pricing information for each product
    '''
    
    url = "https://careers.undercovertourist.com/assignment/1/products/"
    r = requests.get(url,headers=headers)
    request_json = r.json()['results']
    context = {'request_json' : request_json}
    return render(request, 'undercovertourist_app/index.html',context)


    
    
def detail(request, product_id):
    '''
    Display details of the products along with  purchase option if the product has an inventory greater than 1
    '''
    
    url = "https://careers.undercovertourist.com/assignment/1/products/"+str(product_id)+"/"
    try:
        result = requests.get(url,headers=headers).json()
        inventory_on_hand =  True if result['inventory_on_hand'] > 0 else False
        
    except:
        raise Http404("Product Details does not exist")
    context = {'result' : format_html(result['description']),'inventory_on_hand':inventory_on_hand,'id':result['id']}
    return render(request, 'undercovertourist_app/details.html',context)


def purchase(request,product_id):
    
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            url = "https://careers.undercovertourist.com/assignment/1/products/"+product_id+"/purchase"
            data = {
                "customer_email" : form.cleaned_data['customer_email'],
                "customer_name" : form.cleaned_data['customer_name'],
                "customer_phone" : form.cleaned_data['customer_phone'],
                "quantity" : form.cleaned_data['quantity']
                }
            fail_context = {'quantity': form.cleaned_data['quantity'], 'inventory': get_quantity(product_id)}
            if form.cleaned_data['quantity'] > get_quantity(product_id):
                return render(request, 'undercovertourist_app/Fail.html',fail_context)

            result = requests.post(url, data=data, headers=headers)
            print result.json()
            product = get_productdetails(product_id)
            
            customerpurchase = Customer_purchasedata(
                                                    customer_email = form.cleaned_data['customer_email'],
                                                    customer_name = form.cleaned_data['customer_name'],
                                                    customer_phone = form.cleaned_data['customer_phone'],
                                                    product_name = product['name'],
                                                    product_price = product['price'],
                                                    quantity = form.cleaned_data['quantity'],
                                                    confirmation_code = result.json()['confirmation_code'],
                                                    product_id = product_id
                                                    )
            customerpurchase.save()
            success_result = result.json()
            print success_result['confirmation_code']
            print success_result['product']['name']
            success_context = {'confirmation_code':success_result['confirmation_code'],'product':success_result['product']['name']}
            return render(request, 'undercovertourist_app/success.html',success_context)
            
    else:
        form = PurchaseForm(initial={'item_id': product_id})
        

    return render(request, 'undercovertourist_app/purchase.html', {'form': form})


