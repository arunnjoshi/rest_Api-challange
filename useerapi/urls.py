"""useerapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from rest_framework import routers
from myapp.api.views import CreateUserViewset,GetUserViewset,SignIn,PostViewSet
from rest_framework.authtoken.views import  obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
router = routers.DefaultRouter()

router.register("create", CreateUserViewset, basename='create')
router.register('user',GetUserViewset, basename='user')
router.register('signIn',SignIn, basename='signIn')
router.register('post',PostViewSet,basename='post')


urlpatterns = [
    path('api/',include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
]



urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)