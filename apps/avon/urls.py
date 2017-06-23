from django.conf.urls import url
from .views import *


urlpatterns = [
 	url(r'^$',IndexView.as_view(),name='index'),
 	url(r'^ajax-create$',campaing_create,name='create'),
    url(r'^update/(?P<pk>\d+)$',campaing_update,name='update'),
    url(r'^delete/(?P<pk>\d+)$',campaing_delete,name='delete'),
    url(r'^ajax-list/$',ajax_list,name='ajax-list'),


    url(r'^article-create$',article_create,name='create_article'),
    url(r'^delete/article/(?P<id_art>\d+)$',article_delete,name='delete_article'),
    url(r'^detail/(?P<pk>\d+)$',campaing_detail,name='detail'),

    url(r'^detail_customer/$', DetailCustomer.as_view(), name='detail_customer'),
    url(r'^detail_customer/result/$', DetailCustomerResult.as_view(), name='result_customer'),
    url(r'^update/customer/(?P<id_customer>\d+)$', CustomerUpdate, name='update_customer'),
    url(r'^customer-create$',create_customer,name='create_customer'),

    url(r'^customer/list$',ListCustomers.as_view(),name='list_customer'),




]
