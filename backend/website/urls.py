from django.urls import path
from website import views

urlpatterns = [
    path('', views.WebsiteList.as_view(), name='avito-list'),
]