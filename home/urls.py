from django.urls import path, include
from . import views


app_name = 'home'
urlpatterns = [
    #/home
    path('', views.index, name='index'),
    path('mysite/', include('mysite.urls')),
]





