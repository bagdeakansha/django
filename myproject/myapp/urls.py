from django.urls import path,include
from myapp import views

urlpatterns = [
    # path('home/',views.home,name='home'),
    # path('index/',views.home,name='index')
    # path('collection/',views.collection,name='collection')
    # path('filter/',views.filter,name='filter')
    path('form/',views.form,name='form'),
    path('',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('rdata/',views.rdata,name='rdata'),
    path('logout/',views.logout,name='logout'),
    # path('dashboard/',views.dashboard,name='dashboard'),
    
    # path('userlogin/',views.userlogin,name='userlogin'),
]