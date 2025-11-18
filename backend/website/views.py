from django.shortcuts import render
from rest_framework import generics
from website.models import Avito
from .serializers import WebsiteSerializer

from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    # Удрать пагинация при выводе графиков
    # Для построения графиков нужны все данные
    page_size = None
    page_size_query_param = 'page_size'
    max_page_size = 10000


class WebsiteListAll(generics.ListCreateAPIView):
    queryset = Avito.objects.all()
    serializer_class = WebsiteSerializer
    pagination_class = LargeResultsSetPagination


class WebsiteList(generics.ListCreateAPIView):
    queryset = Avito.objects.all()
    serializer_class = WebsiteSerializer
