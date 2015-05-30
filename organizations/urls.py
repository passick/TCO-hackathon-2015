from django.conf.urls import url
from organizations.views import OrganizationsListView

urlpatterns = [
    url(r'^$', OrganizationsListView.as_view(), name='organizations-list'),
]
