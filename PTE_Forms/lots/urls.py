from django.urls import path
from . import views

app_name = 'lots'

urlpatterns = [
    path('',views.ListLot.as_view(), name='all'),
    path('new/',views.CreateLot.as_view(), name='create'),
    path('<slug:slug>/',views.SingleLot.as_view(),name='single'),
]
