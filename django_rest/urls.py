"""django_api_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, reverse
from django.conf.urls import include

from user_app.modules import views_auth
from rest_framework import routers
router = routers.DefaultRouter()
# router.register('', views_auth.HomeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # =============| app endpoints |============
    # path('', views_auth.index_userapp, name='index'),
    path("user/", include("user_app.urls")),
    path("catalog/", include("catalog_app.urls")),

]
