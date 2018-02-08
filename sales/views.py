from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import *
from .forms import *
from datetime import date
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

d = date.today()


def index(request):
    return render(request, 'sales/index.html')


# Add a new customer
class NewCustomer(CreateView):
    model = Customer
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(NewCustomer, self).get_context_data(**kwargs)
        context['manip_type'] = 'Add a New'
        return context


# Edit an existing customer
class EditCustomer(UpdateView):
    model = Customer
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(EditCustomer, self).get_context_data(**kwargs)
        context['manip_type'] = 'Update an Existing'
        return context


# List all the customers
class Customers(ListView):
    model = Customer


# Show details of a specific customer
class CustomerProfile(DetailView):
    model = Customer

    def get_context_data(self, **kwargs):
        context = super(CustomerProfile, self).get_context_data(**kwargs)
        context['customer'] = Customer.objects.get(customer_id=self.kwargs['pk'])
        customer = Customer.objects.get(customer_id=self.kwargs['pk'])
        phone_number = str(customer.phone_number)
        context['phone_number'] = "(" + phone_number[:3] + ") " + phone_number[3:6] + "-" + phone_number [6:]
        context['cust'] = self.kwargs['pk']
        return context


def pre_add_order(request):
    if request.method == 'POST':
        form = PreAddOrderForm(request.POST)
        if form.is_valid():
            cust_id = form.cleaned_data['customer_id']
            return redirect('sales:new_order', cust_id)
    else:
        form = PreAddOrderForm()
    return render(request, 'sales/pre_add_order.html', {'form': form})


# Add a new order
class NewOrder(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('sales:add_items')

    def get_success_url(self):
        return reverse('sales:add_items', args=(self.object.pk, self.kwargs['pk']))

    def get_context_data(self, **kwargs):
        context = super(NewOrder, self).get_context_data(**kwargs)
        context['manip_type'] = 'Add a New'
        return context

    def get_initial(self):
        initial = {}
        initial['customer'] = Customer.objects.get(customer_id=self.kwargs['pk'])
        initial['date_ordered'] = "{}-{}-{}".format(d.year, d.month, d.day)
        return initial


def add_items(request, pk, cust):
    context = {
        'pk': pk,
        'cust': cust,
        'tub_list': QueuedTub.objects.filter(order_id=pk),
        'bottle_list': QueuedBottle.objects.filter(order_id=pk),
    }
    return render(request, 'sales/add_items.html', context)


class NewQueuedTub(CreateView):
    model = QueuedTub
    form_class = NewQueuedTubForm

    def get_success_url(self):
        return reverse('sales:add_items', args=(self.kwargs['pk'],))

    def get_context_data(self, **kwargs):
        context = super(NewQueuedTub, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def get_initial(self):
        initial = {}
        initial['order'] = Order.objects.get(order_number=self.kwargs['pk'])
        return initial

    def form_valid(self, form):
        form.save()


def get_tubs(request, pk):
    tub_set = QueuedTub.objects.filter(order_id=pk)
    return render(request, 'sales/get_tubs.html', {'tub_set': tub_set})


def get_bottles(request, pk):
    bottle_set = QueuedBottle.objects.filter(order_id=pk)
    return render(request, 'sales/get_bottles.html', {'bottle_set': bottle_set})


class NewQueuedBottle(CreateView):
    model = QueuedBottle
    form_class = NewQueuedBottleForm

    def get_context_data(self, **kwargs):
        context = super(NewQueuedBottle, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def get_initial(self):
        initial = {}
        initial['order'] = Order.objects.get(order_number=self.kwargs['pk'])
        return initial

    def form_valid(self, form):
        form.save()
        return render(self.request, 'sales/item_success.html')


# Show details of a specific order
class OrderDetail(DetailView):
    model = Order

    def get_context_data(self, **kwargs):
        context = super(OrderDetail, self).get_context_data(**kwargs)
        context['customer'] = Customer.objects.get(customer_id=self.kwargs['cust'])
        customer = Customer.objects.get(customer_id=self.kwargs['cust'])
        phone_number = str(customer.phone_number)
        context['phone_number'] = "(" + phone_number[:3] + ") " + phone_number[3:6] + "-" + phone_number [6:]
        context['cust'] = self.kwargs['cust']
        context['date'] = d
        tubs = QueuedTub.objects.filter(order_id=self.kwargs['pk'])
        used_tubs = []
        context["tubs"] = {}
        for tub in tubs:
            if tub.fill not in used_tubs:
                context["tubs"]["{}".format(tub.fill)] = [1, "Unit", tub.fill, 400, 400]
                used_tubs.append("{}".format(tub.fill))
            else:
                context["tubs"]["{}".format(tub.fill)][0] += 1
                context["tubs"]["{}".format(tub.fill)][4] += 400
        bottles = QueuedBottle.objects.filter(order_id=self.kwargs['pk'])
        used_bottles = []
        context["bottles"] = {}
        for bottle in bottles:
            cur_bottle = bottle.fill + bottle.size
            if cur_bottle not in used_bottles:
                context["bottles"]["{}".format(cur_bottle)] = [1, "Unit", " - ".join([bottle.fill, bottle.size]), 20, 20]
                used_bottles.append("{}".format(cur_bottle))
            else:
                context["bottles"]["{}".format(cur_bottle)][0] += 1
                context["bottles"]["{}".format(cur_bottle)][4] += 20
        context['tub_total'] = QueuedTub.objects.filter(order_id=self.kwargs['pk']).count() * 400
        context['bottle_total'] = QueuedBottle.objects.filter(order_id=self.kwargs['pk']).count() * 20
        subtotal = context['tub_total'] + context['bottle_total']
        context['subtotal'] = subtotal
        tax = subtotal * .07
        context['tax'] = "{:.2f}".format(tax)
        total = subtotal + tax
        context['total'] = "{:.2f}".format(total)

        return context
