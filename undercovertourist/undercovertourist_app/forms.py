from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.
from CodeWarrior import Required
from utils import *
    
class PurchaseForm(forms.Form):
   # renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
    customer_email = forms.EmailField() 
    customer_name = forms.CharField()
    customer_phone = forms.CharField()
    quantity = forms.IntegerField()
    #item_id = forms.IntegerField(widget = forms.HiddenInput())
    item_id = forms.IntegerField()
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        
        #Check date is not in past. 
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        #Check date is in range librarian allowed to change (+4 weeks).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data
    '''def clean_quantity(self):
        quantity_data = self.cleaned_data['quantity']
        inventory_on_hand = get_quantity(self.cleaned_data['item_id'])
        if quantity_data > inventory_on_hand:
            raise ValidationError(_('Invetory on hand is only: '+ inventory_on_hand))
        return quantity_data'''
        
        