# count_click/urls.py

from django.urls import path
from .views import ClickAPIView

urlpatterns = [
    # count_clicks/click/ 으로 쏴주세용
    # project urls.py에 count_clicks/ => include(지금 이 파일)
    path('click/', ClickAPIView.as_view(), name='click'),
]
