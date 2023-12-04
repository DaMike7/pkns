from django.urls import path
from . import views
#app_name = 'kids'

urlpatterns = [
    path('',views.kidsList,name='kids_list'),
    path('register/',views.registerKid,name="new_kid"),
    path('login/',views.userLogin,name='login_page'),
    path('logout/',views.userLogout,name='logout_page'),
    path('<slug:handle>/',views.kidDetail,name="kid_profile"),
]