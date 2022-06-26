import imp
from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.db import router
from django.urls import path,include
# from .views import fun
from .views import *
from productMaster import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("product",views.productData)

# router.register('productUpdate',views.productUpdate)


urlpatterns= [ 

    path('',include(router.urls))

    # path('index/',fun)

]