from django.shortcuts import render
from rest_framework import generics
from website.models import Avito
from .serializers import WebsiteSerializer

from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    # Удрать пагинация при выводе графиков
    # Для построения графиков нужны все данные
    page_size = None
    # page_size_query_param = 'page_size'
    # max_page_size = 10000


class WebsiteListAll(generics.ListCreateAPIView):
    queryset = Avito.objects.all()
    serializer_class = WebsiteSerializer
    pagination_class = LargeResultsSetPagination


class WebsiteList(generics.ListCreateAPIView):
    # sort_order = request.query_params.get('your_key_name', None)
    # queryset = Avito.objects.all()
    serializer_class = WebsiteSerializer

    def get_queryset(self):
        queryset = Avito.objects.all()
        sort_price_order = self.request.query_params.get('sort_price_order', None)

        if sort_price_order == "DESC":
            queryset = queryset.order_by("-rating_all")
        elif sort_price_order == "ASC":
            queryset = queryset.order_by("rating_all")

        return queryset