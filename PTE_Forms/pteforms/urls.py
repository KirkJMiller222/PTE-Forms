from django.urls import path, include
from . import views


app_name = 'pteforms'

urlpatterns = [
    path('',views.GramStainList.as_view(), name='all'),
    path('newgramstain/',views.CreateGramStain.as_view(), name='create'),
    path('lot/<lot_number>/>',views.LotGramStain.as_view(), name='for_lot'),
    path('lot/<lot_number>/<int:pk>',views.GramStainDetail.as_view(), name='single'),
    path('delete/<int:pk>',views.DeleteGramStain.as_view(), name='delete'),

]
