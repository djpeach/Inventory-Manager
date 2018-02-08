from django.conf.urls import url
from . import views

app_name="sales"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # url(r'^add_order_customer', views.add_order_customer, name='add_order_customer'),
    # url(r'^add_order/(?P<customer_id>[0-9]+)/$', views.OrderAdd.as_view(), name='add_order'),
    # url(r'^pre_order_update/$', views.pre_order_update, name='pre_order_update'),
    # url(r'^order_update/(?P<order_number>[0-9]+)$', views.order_update, name='order_update'),
    url(r'^customers/$', views.Customers.as_view(), name='customers'),
    url(r'^customers/(?P<pk>[0-9]+)/$', views.CustomerProfile.as_view(), name='customer_details'),
    url(r'^customers/new/$', views.NewCustomer.as_view(), name='new_customer'),
    url(r'^customer/update/(?P<pk>[0-9]+)/$', views.EditCustomer.as_view(), name='edit_customer'),
    url(r'^orders/pre_add_order$', views.pre_add_order, name='pre_add_order'),
    url(r'^orders/new/(?P<pk>[0-9]+)/$', views.NewOrder.as_view(), name='new_order'),
    url(r'^orders/new/(?P<pk>[0-9]+)/new_queued_tub/$', views.NewQueuedTub.as_view(), name='new_queued_tub'),
    url(r'^orders/new/(?P<pk>[0-9]+)/new_queued_bottle/$', views.NewQueuedBottle.as_view(), name='new_queued_bottle'),
    url(r'^orders/(?P<cust>[0-9]+)/(?P<pk>[0-9]+)/$', views.OrderDetail.as_view(), name='order_detail'),
    url(r'^orders/(?P<pk>[0-9]+)/(?P<cust>[0-9]+)/add_items', views.add_items, name='add_items'),
    url(r'^orders/(?P<pk>[0-9]+)/get_tubs', views.get_tubs, name='get_tubs'),
    url(r'^orders/(?P<pk>[0-9]+)/get_bottles', views.get_bottles, name='get_bottles'),

]
