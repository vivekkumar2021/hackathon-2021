from django.urls import path
from hack import views
urlpatterns = [
    path("", views.index, name="index"),
    path("verticals", views.verticals, name="verticals"),
    path("agriculture", views.agriculture, name="agriculture"),
    path("banking", views.banking, name="banking"),
    path("bd", views.bd, name="bd"),
    path("fintech", views.fintech, name="fintech"),
    path("hospitality", views.hospitality, name="hospitality"),
    path("hr", views.hr, name="hr"),
    path("insurance", views.insurance, name="insurance"),
    path("inventory", views.inventory, name="inventory"),
    path("manufacturing", views.manufacturing, name="manufacturing"),
    path("marketing", views.marketing, name="marketing"),
    path("pharma", views.pharma, name="pharma"),
    path("retail", views.retail, name="retail"),
    path("telecom", views.telecom, name="telecom"),
    path("travel", views.travel, name="travel"),
    path("utilities", views.utilities, name="utilities"),
]