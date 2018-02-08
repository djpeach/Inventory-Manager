from django.conf.urls import url, include
from . import views

app_name="warehouse"

urlpatterns = [

    # ==================== INDEX ==================== #
    url(r'^$', views.index, name="index"),

    # ==================== BOTTLES ==================== #
    url(r'^bottles/$', views.bottles, name='bottles'),
    url(r'^bottles/add/$', views.BottlesAdd.as_view(), name='bottles_add'),
    url(r'^bottles/pre_update/$', views.pre_bottles_update, name='pre_bottles_update'),
    url(r'^bottles/update/(?P<pk>\w+)$', views.BottlesUpdate.as_view(), name='bottles_update'),
    url(r'^bottles/pre_remove/$', views.pre_bottles_remove, name='pre_bottles_remove'),
    url(r'^bottles/remove/(?P<pk>\w+)$', views.BottlesRemove.as_view(), name='bottles_remove'),

    # ==================== TUBS ==================== #
    url(r'^tubs/$', views.tubs, name='tubs'),
    url(r'^tubs/add/$', views.TubsAdd.as_view(), name='tubs_add'),
    url(r'^tubs/pre_update/$', views.pre_tubs_update, name='pre_tubs_update'),
    url(r'^tubs/update/(?P<pk>\w+)$', views.TubsUpdate.as_view(), name='tubs_update'),
    url(r'^tubs/pre_remove/$', views.pre_tubs_remove, name='pre_tubs_remove'),
    url(r'^tubs/remove/(?P<pk>\w+)$', views.TubsRemove.as_view(), name='tubs_remove'),

    # ==================== ORDERS ==================== #
    url(r'^orders/$', views.orders, name='orders'),
    url(r'^orders/pre-ship/$', views.pre_ship, name='pre_ship_order'),
    url(r'^orders/pre-return', views.pre_return, name='pre_return_order'),
    url(r'^orders/(?P<order_num>[0-9]+)/ship/$', views.ship_order, name='order_ship'),
    url(r'^orders/(?P<order_num>[0-9]+)/return/$', views.return_order, name='order_return'),
    url(r'^orders/(?P<order_num>[0-9]+)/ship/add_tub', views.add_order_tub, name='add_order_tub'),
    url(r'^orders/(?P<order_num>[0-9]+)/ship/add_bottle', views.add_order_bottle, name='add_order_bottle'),
    url(r'^orders/(?P<order_num>[0-9]+)/ship/return_tub', views.return_order_tub, name='return_order_tub'),
    url(r'^orders/(?P<order_num>[0-9]+)/ship/return_bottle', views.return_order_bottle, name='return_order_bottle'),
]
