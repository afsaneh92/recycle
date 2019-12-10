from django.conf.urls import url
# from django.urls import path
from . import views

app_name = 'collector'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^requests/$', views.RequestListView.as_view(), name='requests_list'),
    url(r'^request_detail/$', views.RequestDetailView.as_view(), name='request_detail'),
    url(r'^receivers/$', views.ReceiverListView.as_view(), name='receivers_list'),
    url(r'^receiver/create/$', views.receiver_create, name='add_receiver'),
    url(r'^receiver/detail/(?P<pk>\d+)$', views.receiver_detail, name='receiver_detail'),
    url(r'^receiver/edit/(?P<pk>\d+)$', views.receiver_edit, name='edit_receiver'),
    url(r'^receiver/delete/$', views.receiver_delete, name='delete_receiver'),

]
