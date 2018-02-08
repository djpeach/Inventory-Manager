from django import forms
from inventory.models import *


# ==================== TUBS FORMS ==================== #

# Form class for adding tubs, overriding the default one
class TubsAddForm(forms.ModelForm):
    # Override the default __init__ to add .widget.attrs css to each field
    def __init__(self, *args, **kwargs):
        super(TubsAddForm, self).__init__(*args, **kwargs)
        self.fields['emp_init'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['fill'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['status'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['serial_number'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['barcode'].widget.attrs = {
            'class': 'form-control'
        }

    # Meta data here tells the class what model to use, and what fields to use
    class Meta:
        model = Tub
        fields = ['emp_init', 'fill', 'status', 'serial_number', 'barcode']


# Form for getting tub barcode pre-updating it
class PreTubsUpdateForm(forms.Form):
    barcode = forms.CharField(label='Barcode', max_length=15, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))


class TubsUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TubsUpdateForm, self).__init__(*args, **kwargs)
        self.fields['order'].required = False
        self.fields['emp_init'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['fill'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['status'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['serial_number'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['barcode'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['order'].widget.attrs = {
            'class': 'form-control'
        }

    class Meta:
        model = Tub
        fields = '__all__'


# Form for getting tub barcode pre-removing it
class PreTubsRemoveForm(forms.Form):
    barcode = forms.CharField(label='Barcode', max_length=15, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))


# ==================== BOTTLES FORMS ==================== #

# Form class for adding tubs, overriding the default one
class BottlesAddForm(forms.ModelForm):
    # Override the default __init__ to add .widget.attrs css to each field
    def __init__(self, *args, **kwargs):
        super(BottlesAddForm, self).__init__(*args, **kwargs)
        self.fields['emp_init'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['fill'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['size'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['status'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['serial_number'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['barcode'].widget.attrs = {
            'class': 'form-control'
        }

    # Meta data here tells the class what model to use, and what fields to use
    class Meta:
        model = Bottle
        fields = ['emp_init', 'fill', 'serial_number', 'size', 'status', 'barcode']


# Form for getting tub barcode pre-updating it
class PreBottlesUpdateForm(forms.Form):
    barcode = forms.CharField(label='Barcode', max_length=15, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))


class BottlesUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BottlesUpdateForm, self).__init__(*args, **kwargs)
        self.fields['order'].required = False
        self.fields['emp_init'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['fill'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['size'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['status'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['serial_number'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['barcode'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['order'].widget.attrs = {
            'class': 'form-control'
        }

    class Meta:
        model = Bottle
        fields = '__all__'


# Form for getting tub barcode pre-removing it
class PreBottlesRemoveForm(forms.Form):
    barcode = forms.CharField(label='Barcode', max_length=15, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))

# ==================== ORDERS FORMS ==================== #


class AddOrderTubForm(forms.Form):
    barcode = forms.CharField(label='Barcode', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))


class AddOrderBottleForm(forms.Form):
    barcode = forms.CharField(label='Barcode', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))


class PreShipForm(forms.Form):
    order_number = forms.CharField(label='Order Number', max_length=15, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))


class PreReturnForm(forms.Form):
    barcode = forms.CharField(label='Item Barcode', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))


class ReturnOrderTubForm(forms.Form):
    barcode = forms.CharField(label='Barcode', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))


class ReturnOrderBottleForm(forms.Form):
    barcode = forms.CharField(label='Barcode', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))