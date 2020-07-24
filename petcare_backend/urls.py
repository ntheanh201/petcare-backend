from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from petcare import views

# Routers provide an easy way of automatically determining the URL conf.
from petcare.views import (
    ProductViewSet,
    PetcareUserViewSet,
    ShopViewSet,
    ReviewViewSet,
    SaleViewSet,
    OrderViewSet,
    ChatViewSet,
    ClinicViewSet,
    CustomerViewSet,
    AdminViewSet,
    CartViewSet,
)

ROUTER = routers.DefaultRouter()
ROUTER.register(r"users", PetcareUserViewSet)
ROUTER.register(r"products", ProductViewSet)
ROUTER.register(r"sales", SaleViewSet)
ROUTER.register(r"shops", ShopViewSet)
ROUTER.register(r"customers", CustomerViewSet)
ROUTER.register(r"admins", AdminViewSet)
ROUTER.register(r"orders", OrderViewSet)
ROUTER.register(r"reviews", ReviewViewSet)
ROUTER.register(r"clinics", ClinicViewSet)
ROUTER.register(r"carts", CartViewSet)
ROUTER.register(r"chats", ChatViewSet)


urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", include(ROUTER.urls)),
        path("auth/", include("djoser.urls")),
        path("auth/", include("djoser.urls.jwt")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
