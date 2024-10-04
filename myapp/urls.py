from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('count', views.count, name='count'),
   path('register', views.register, name='register'),
    # path('ww', views.ww, name='ww')
    
]
