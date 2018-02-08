from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/', include('dashboard.urls', namespace='dashboard')),
    url(r'^sales/', include('sales.urls', namespace='sales')),
    url(r'^warehouse/', include('warehouse.urls', namespace='warehouse')),

    # ==================== TESTING PURPOSES ==================== #
    url(r'^testing/$', views.testing, name='testing'),
    url(r'^add_tubs/$', views.add_tubs, name='add_tubs'),
    url(r'^del_tubs/$', views.del_tubs, name='del_tubs'),
    url(r'^add_bottles/$', views.add_bottles, name='add_bottles'),
    url(r'^del_bottles/$', views.del_bottles, name='del_bottles'),
    url(r'^add_customers/$', views.add_customers, name='add_customers'),
    url(r'^del_customers/$', views.del_customers, name='del_customers'),
    url(r'^add_orders/$', views.add_orders, name='add_orders'),
    url(r'^del_orders/$', views.del_orders, name='del_orders'),
]
