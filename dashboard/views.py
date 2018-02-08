from django.shortcuts import render
from inventory.models import *


def index(request):
    # Tubs
    all_tubs = Tub.objects.all()
    shop_tubs = Tub.objects.filter(status__contains='D').count()
    total_tubs = Tub.objects.count()
    out_tubs = total_tubs - shop_tubs
    shop_tubs_percent = int("{:.0f}".format((shop_tubs / total_tubs) * 100))
    out_tubs_percent = int("{:.0f}".format(100 - shop_tubs_percent))

    # Bottles
    all_bottles = Bottle.objects.all()
    shop_bottles = Bottle.objects.filter(status__contains='D').count()
    total_bottles = Bottle.objects.count()
    out_bottles = total_bottles - shop_bottles
    shop_bottles_percent = int("{:.0f}".format((shop_bottles / total_bottles) * 100))
    out_bottles_percent = int("{:.0f}".format(100 - shop_bottles_percent))

    # Orders
    all_orders = Order.objects.all()
    out_orders = Order.objects.filter(status='SHIPPED').count()
    total_orders = Order.objects.count()
    shop_orders = total_orders - out_orders
    shop_orders_percent = int("{:.0f}".format((shop_orders / total_orders) * 100))
    out_orders_percent = int("{:.0f}".format(100 - shop_orders_percent))
    context = {
        'all_tubs': all_tubs,
        'shop_tubs': shop_tubs,
        'total_tubs': total_tubs,
        'out_tubs': out_tubs,
        'shop_tubs_percent': shop_tubs_percent,
        'out_tubs_percent': out_tubs_percent,
        'all_bottles': all_bottles,
        'shop_bottles': shop_bottles,
        'total_bottles': total_bottles,
        'out_bottles': out_bottles,
        'shop_bottles_percent': shop_bottles_percent,
        'out_bottles_percent': out_bottles_percent,
        'all_orders': all_orders,
        'shop_orders': shop_orders,
        'total_orders': total_orders,
        'out_orders': out_orders,
        'shop_orders_percent': shop_orders_percent,
        'out_orders_percent': out_orders_percent,
    }
    return render(request, 'dashboard/index.html', context)
