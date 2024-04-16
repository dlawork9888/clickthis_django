# Project/urls.py
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("count_clicks/", include('count_clicks.urls')) # count_clicks 앱 urls.py
]
