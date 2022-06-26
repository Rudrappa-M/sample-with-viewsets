from itertools import product
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import product
from .serializers import *
# Create your views here.
# def fun(request):
#     return HttpResponse('this is My first project')

class productData(viewsets.ModelViewSet):
    queryset=product.objects.all()
    serializer_class=productSerializer
    http_method_names=['post','get','put','delete']

