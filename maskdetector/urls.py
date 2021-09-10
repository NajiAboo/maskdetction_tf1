from maskdetector.views import PredictMas, index
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

 

urlpatterns = [
    path('', index),
    path('/predict', PredictMas.as_view(), name='predict'),
]
