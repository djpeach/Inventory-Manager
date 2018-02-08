from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
from sales.models import *
from inventory.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse


# ==================== INDEX ==================== #
def index(request):
    return render(request, 'warehouse/index.html')


# ==================== TUBS ==================== #
def tubs(request):
    return render(request, 'warehouse/tubs.html')


class TubsAdd(CreateView):
    model = Tub
    form_class = TubsAddForm


def pre_tubs_update(request):
    if request.method == 'POST':
        form = PreTubsUpdateForm(request.POST)
        if form.is_valid():
            barcode = form.cleaned_data['barcode']
            serial_number = Tub.objects.get(barcode=barcode).serial_number
            # calls a url with a namespace, which calls a view, both get the serial number
            return redirect('warehouse:tubs_update', serial_number)
    else:
        form = PreTubsUpdateForm()
    return render(request, 'warehouse/pre_tub_update.html', {'form': form})


class TubsUpdate(UpdateView):
    model = Tub
    form_class = TubsUpdateForm
    template_name_suffix = '_update_form'


def pre_tubs_remove(request):
    if request.method == 'POST':
        form = PreTubsRemoveForm(request.POST)
        if form.is_valid():
            barcode = form.cleaned_data['barcode']
            serial_number = Tub.objects.get(barcode=barcode).serial_number
            return redirect('warehouse:tubs_remove', serial_number)
    else:
        form = PreTubsRemoveForm()
    return render(request, 'warehouse/pre_tub_remove.html', {'form': form})


class TubsRemove(DeleteView):
    model = Tub
    success_url = reverse_lazy('warehouse:tubs')


# ==================== BOTTLES ==================== #
def bottles(request):
    return render(request, 'warehouse/bottles.html')


class BottlesAdd(CreateView):
    model = Bottle
    form_class = BottlesAddForm


def pre_bottles_update(request):
    if request.method == 'POST':
        form = PreBottlesUpdateForm(request.POST)
        if form.is_valid():
            barcode = form.cleaned_data['barcode']
            serial_number = Bottle.objects.get(barcode=barcode).serial_number
            # calls a url with a namespace, which calls a view, both get the serial number
            return redirect('warehouse:bottles_update', serial_number)
    else:
        form = PreBottlesUpdateForm()
    return render(request, 'warehouse/pre_bottle_update.html', {'form': form})


class BottlesUpdate(UpdateView):
    model = Bottle
    form_class = BottlesUpdateForm
    template_name_suffix = '_update_form'


def pre_bottles_remove(request):
    if request.method == 'POST':
        form = PreBottlesRemoveForm(request.POST)
        if form.is_valid():
            barcode = form.cleaned_data['barcode'].upper()
            serial_number = Bottle.objects.get(barcode=barcode).serial_number
            return redirect('warehouse:bottles_remove', serial_number)
    else:
        form = PreBottlesRemoveForm()
    return render(request, 'warehouse/pre_bottle_remove.html', {'form': form})


class BottlesRemove(DeleteView):
    model = Bottle
    success_url = reverse_lazy('warehouse:bottles')


# ==================== ORDERS ==================== #
def orders(request):
    return render(request, 'warehouse/orders.html')


def pre_ship(request):
    if request.method == 'POST':
        form = PreShipForm(request.POST)
        if form.is_valid():
            order_number = form.cleaned_data['order_number']
            return redirect('warehouse:order_ship', order_number)
    else:
        form = PreShipForm()
    return render(request, 'warehouse/pre-ship.html', {'form': form})


def ship_order(request, order_num):
    if request.method == 'POST':
        a = Order.objects.get(order_number=order_num)
        a.status = 'SHIPPED'
        a.save()
        return render(request, 'warehouse/orders.html')
    else:
        order = Order.objects.get(order_number=order_num)
        queued_bottles = QueuedBottle.objects.filter(order_id=order_num)
        queued_tubs = QueuedTub.objects.filter(order_id=order_num)
        added_bottles = Bottle.objects.filter(order=order, )
        added_tubs = Tub.objects.filter(order=order)
        context = {
            'order': order,
            'queued_bottles': queued_bottles,
            'queued_tubs': queued_tubs,
            'order_num': order_num,
            'added_bottles': added_bottles,
            'added_tubs': added_tubs,
        }
        return render(request, 'warehouse/ship-order.html', context)


def add_order_tub(request, order_num):
    if request.method == 'POST':
        form = AddOrderTubForm(request.POST)
        if form.is_valid():
            barcode = form.cleaned_data['barcode']
            tub = Tub.objects.get(barcode=barcode)
            order = Order.objects.get(order_number=order_num)
            tub.order = order
            tub.status = 'CS'
            tub.save()
            return redirect('warehouse:order_ship', order_num)
    else:
        form = AddOrderTubForm()
    return render(request, 'warehouse/add_order_tub.html', {'form': form, 'order_num': order_num})


def add_order_bottle(request, order_num):
    if request.method == 'POST':
        form = AddOrderBottleForm(request.POST)
        if form.is_valid():
            barcode = form.cleaned_data['barcode']
            bottle = Bottle.objects.get(barcode=barcode)
            order = Order.objects.get(order_number=order_num)
            bottle.order = order
            bottle.status = 'CS'
            bottle.save()
            return redirect('warehouse:order_ship', order_num)
    else:
        form = AddOrderBottleForm()
    return render(request, 'warehouse/add_order_bottle.html', {'form': form, 'order_num': order_num})


def pre_return(request):
    if request.method == 'POST':
        form = PreReturnForm(request.POST)
        if form.is_valid():
            barcode = form.cleaned_data['barcode']
            try:
                item = Bottle.objects.get(barcode=barcode)
            except ObjectDoesNotExist:
                item = Tub.objects.get(barcode=barcode)
            order_number = item.order.order_number
            return redirect('warehouse:order_return', order_number)
    else:
        form = PreReturnForm()
    return render(request, 'warehouse/pre-return.html', {'form': form})


def return_order(request, order_num):
    order = Order.objects.get(order_number=order_num)
    added_bottles = Bottle.objects.filter(order_id=order_num, status='CS')
    added_tubs = Tub.objects.filter(order_id=order_num, status='CS')
    returned_bottles = Bottle.objects.filter(order=order, status='DE')
    returned_tubs = Tub.objects.filter(order=order, status='DE')
    order_number = order.order_number
    context = {
        'order': order,
        'added_bottles': added_bottles,
        'added_tubs': added_tubs,
        'order_num': order_number,
        'returned_tubs': returned_tubs,
        'returned_bottles': returned_bottles
    }
    return render(request, 'warehouse/return-order.html', context)


def return_order_tub(request, order_num):
    if request.method == 'POST':
        form = ReturnOrderTubForm(request.POST)
        if form.is_valid():
            barcode = form.cleaned_data['barcode']
            tub = Tub.objects.get(barcode=barcode)
            tub.status = 'DE'
            tub.save()
            return redirect('warehouse:order_return', order_num)
    else:
        form = ReturnOrderTubForm()
    return render(request, 'warehouse/return_order_tub.html', {'form': form, 'order_num': order_num})


def return_order_bottle(request, order_num):
    if request.method == 'POST':
        form = ReturnOrderBottleForm(request.POST)
        if form.is_valid():
            barcode = form.cleaned_data['barcode']
            bottle = Bottle.objects.get(barcode=barcode)
            order = Order.objects.get(order_number=order_num)
            bottle.order = order
            bottle.status = 'DE'
            bottle.save()
            return redirect('warehouse:order_return', order_num)
    else:
        form = ReturnOrderBottleForm()
    return render(request, 'warehouse/return_order_bottle.html', {'form': form, 'order_num': order_num})