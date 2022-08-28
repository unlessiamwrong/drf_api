"""drf_api URL Configuration

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
from django.urls import path
from django.conf.urls import include
from items.urls import urlpatterns as items_url
from carts.urls import urlpatterns as carts_url
from users.urls import urlpatterns as users_url
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from items.views import UserViewset

schema_view = get_schema_view(
    openapi.Info(
        title='Stepic DRF API',
        default_version='v1',
    ),
    public=True,
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path(r'api/v1/', include(items_url)),
    path(r'api/v1/', include(carts_url)),
    path(r'users/', include(users_url)),

]
