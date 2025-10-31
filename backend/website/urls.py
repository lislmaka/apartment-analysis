from django.urls import path
from website import views

urlpatterns = [
    path('list/', views.WebsiteList.as_view(), name='avito-list'),
]