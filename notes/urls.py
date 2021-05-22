from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.shortcuts import render


def vtests(request):
    return render(request, 'tests.html')


urlpatterns = [
    path('', vtests),
]
