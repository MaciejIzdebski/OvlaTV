"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'telephones', views.TelephoneViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'persons', views.PersonViewSet)
router.register(r'addresses', views.AddressViewSet)
router.register(r'employees', views.EmployeeViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('', admin.site.urls),
]
