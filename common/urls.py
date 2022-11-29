
from django.urls import path
from .import views
app_name='common'

urlpatterns = [
    
    path('', views.common_home, name='index'),
     path('shorts', views.common_shorts,name='shorts'),
]