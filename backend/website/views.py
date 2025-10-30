from django.shortcuts import render
from rest_framework import generics
from website.models import Avito
from .serializers import WebsiteSerializer


class WebsiteList(generics.ListCreateAPIView):
    queryset = Avito.objects.all()
    serializer_class = WebsiteSerializer
