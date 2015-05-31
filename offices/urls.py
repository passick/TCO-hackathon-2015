from django.conf.urls import include, url
from offices.views import OfficeView, OfficeListView

urlpatterns = [
    url(r'^$', OfficeListView.as_view(), name='office_list'),
    url(r'^(?P<pk>[0-9]+)$', OfficeView.as_view(), name='office_info'),
]
