from django.conf.urls import url
from company import views

urlpatterns = [
    url(r'^$', views.stocks, name="stocks"),
    url(r'^price/(?P<category>\w+)$', views.get_price, name="price"),
    url(r'^invoice/$', views.generate_invoice, name="invoice"),
    url(r'^business/$', views.business, name="business"),
    url(r'^employees/$', views.employees, name="employees"),
    url(r'^categories/(?P<product>\w+)$', views.get_categories, name="categories"),
]