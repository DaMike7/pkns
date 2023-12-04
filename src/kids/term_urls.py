from django.urls import path
from . import views

urlpatterns=[
    path('',views.termList,name='term_list'),
    path('<slug:handle>/',views.termDetail,name='term_info'),
]