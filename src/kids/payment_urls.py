from django.urls import path
from . import views

urlpatterns=[
    path('',views.paymentList,name='payment_list'),
    path('new/',views.addPayment,name='add_payment'),
    path('<slug:handle>/',views.paymentDetail,name='payment_details'),
]