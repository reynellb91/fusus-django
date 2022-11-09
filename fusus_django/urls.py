"""fusus_django URL Configuration

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
from django.urls import path

from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from organizations.views import UserViewSet, OrganizationViewSet, GroupsViewSet, InfoApiView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = SimpleRouter()
router.register("api/auth/groups", GroupsViewSet)
router.register("api/users", UserViewSet)
router.register("api/organizations", OrganizationViewSet)

organizations_router = NestedSimpleRouter(router, 'api/organizations', lookup='organization')
organizations_router.register('users', UserViewSet, basename='organization-users')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/info/', InfoApiView.as_view()),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
urlpatterns += organizations_router.urls