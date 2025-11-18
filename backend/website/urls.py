from django.urls import path
from website import views

urlpatterns = [
    path('lists/', views.WebsiteListAll.as_view(), name='avito-lists'),
    path('list/', views.WebsiteList.as_view(), name='avito-list'),
]