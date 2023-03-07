from django.urls import path,include
from .views import home,signup


urlpatterns = [
        path('',home,name='home'),
        path('signp/',signup,name='signup'),
        path('accounts/',include('django.contrib.auth.urls')),
       
]
