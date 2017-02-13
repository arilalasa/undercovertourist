import requests
import json
from django.http import HttpResponse, Http404,HttpResponseRedirect
headers = {'X-Auth': '{lalasa}.{ari}'}


def get_quantity(product_id):
    url = "https://careers.undercovertourist.com/assignment/1/products/"+str(product_id)+"/"
    
    result = requests.get(url,headers=headers).json()
    #inventory_on_hand =  True if result['inventory_on_hand'] > 0 else False
    print("inventory on hand " + str(result['inventory_on_hand']))
    return result['inventory_on_hand']

def get_productdetails(product_id):
    url = "https://careers.undercovertourist.com/assignment/1/products/"+str(product_id)+"/"
    try:
        result = requests.get(url,headers=headers).json()
        print(result)
           
    except:
        raise Http404("Product Details does not exist")
    context = {'name' : result['name'],'price': result['price'],'id':result['id']}
    return context