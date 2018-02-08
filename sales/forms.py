from django import forms
from .models import *
from inventory.models import Bottle, Tub
from django.contrib.admin.widgets import AdminDateWidget


# Custom Form for New Orders
class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['date_ordered'].widget.attrs = {
            'class': 'form-control', 'readonly': 'readonly'
        }
        self.fields['ship_date'].widget.attrs={
            'class': 'form-control'
        }
        self.fields['emp_init'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['customer'].widget.attrs = {
            'class': 'form-control', 'readonly': 'readonly'
        }
        self.fields['po_number'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['branch'].widget.attrs = {
            'class': 'form-control', 'readonly': 'readonly'
        }
        self.fields['ship_method'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['courier'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['order_type'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['status'].widget.attrs = {
            'class': 'form-control', 'readonly': 'readonly'
        }

    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'customer': forms.TextInput(),
            'status': forms.TextInput(),
        }
        labels = {
            'po_number': 'PO Number',
            'customer': 'Customer ID',
        }


class GetCustomer(forms.Form):
    customer_id = forms.CharField(label='Customer Number', max_length=15, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))


class PreAddOrderForm(forms.Form):
    customer_id = forms.CharField(label='Customer Number', max_length=15, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))


class NewQueuedTubForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewQueuedTubForm, self).__init__(*args, **kwargs)
        self.fields['fill'].widget.attrs = {
            'class': 'form-control',
        }
        self.fields['order'].widget.attrs={
            'class': 'form-control', 'readonly': 'readonly'
        }

    class Meta:
        model = QueuedTub
        fields = '__all__'
        widgets = {
            'order': forms.TextInput(),
        }

class NewQueuedBottleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewQueuedBottleForm, self).__init__(*args, **kwargs)
        self.fields['fill'].widget.attrs = {
            'class': 'form-control',
        }
        self.fields['size'].widget.attrs = {
            'class': 'form-control',
        }
        self.fields['order'].widget.attrs = {
            'class': 'form-control', 'readonly': 'readonly'
        }

    class Meta:
        model = QueuedBottle
        fields = '__all__'
        widgets = {
            'order': forms.TextInput(),
        }

class OrderAddBottle(forms.Form):
    size = forms.ChoiceField(label='Size', choices=Bottle.SIZE_CHOICES)
    size.widget.attrs={'class': 'form-control'}
    fill = forms.ChoiceField(label='Fill Type', choices=Bottle.FILL_CHOICES)
    fill.widget.attrs = {'class': 'form-control'}
    hm = forms.IntegerField(label="Quantity")
    hm.widget.attrs = {'class': 'form-control'}


class QueuedTubForm(forms.Form):
    fill = forms.ChoiceField(label='Fill Type', choices=Tub.FILL_CHOICES)
    fill.widget.attrs = {'class': 'form-control'}
    hm = forms.IntegerField(label="Quantity")
    hm.widget.attrs = {'class': 'form-control'}
    class Meta:
        model = QueuedTub
        fields = '__all__'


