from django.test import TestCase
from django.test.client import Client
from rebar.testing import flatten_to_dict
from forms import *
from models import *
# Create your tests here.
'''
We have to install Rebar, as I have used one of their testing utilities.
Rebar is a collection of utilities for working with Forms. We’ll install Rebar so we can use the testing utilities.

$ pip install rebar
'''

class Customer_purchasedataTests(TestCase):
    '''
    Test for testing DB of table Customer_purchasedata
    '''
    def test_str(self):

        purchase = Customer_purchasedata(
                                        customer_email = 'test123@gmail.com',
                                        customer_name = 'test123',
                                        customer_phone = '5123435565',
                                        product_name = 'product1',
                                        product_price = 20,
                                        
                                        )
        purchase.save()

        self.assertEquals(
            str(purchase),
            'test123',
        )
        
class Touristplaces_list(TestCase):
    def test_touristplaceslist(self):
        client = Client()
        response = client.get('/undercovertourist/')
        print(response.context['request_json'])
        self.assertEquals(len(response.context['request_json']), 100)
        

class EditContactFormTests(TestCase):

    def test_mismatch_email_is_invalid(self):

        form_data = flatten_to_dict(forms.PurchaseForm())
        form_data['customer_email'] = 'abc123@gmail'
        form_data['customer_name'] = 'foo'
        form_data['customer_phone'] = '5112435544'
        form_data['qunatity'] = 1
        form_data['item_id'] = 101
        
        bound_form = forms.PurchaseForm(data=form_data)
        self.assertFalse(bound_form.is_valid())

    def test_same_email_is_valid(self):

        form_data = flatten_to_dict(forms.PurchaseForm())
        form_data['customer_email'] = 'abc123@gmail.com'
        form_data['customer_name'] = 'foo'
        form_data['customer_phone'] = '5112435544'
        form_data['qunatity'] = 1
        form_data['item_id'] = 101
        

        bound_form = forms.PurchaseForm(data=form_data)
        self.assert_(bound_form.is_valid())