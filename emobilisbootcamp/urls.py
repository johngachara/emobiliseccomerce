from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='home'),
    path('shop/',views.shoppage,name='shop'),
    path('about/',views.aboutuspage,name='aboutus')
]