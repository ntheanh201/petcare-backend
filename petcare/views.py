from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions

# custom TokenObtain view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from petcare.models import (
    Product,
    PetcareUser,
    Review,
    Sale,
    Shop,
    Order,
    Cart,
    Customer,
    Admin,
    Chat,
    Clinic,
)
from petcare.serializers import (
    ProductSerializer,
    PetcareMemberSerializer,
    ShopSerializer,
    ReviewSerializer,
    SaleSerializer,
    OrderSerializer,
    CartSerializer,
    CustomerSerializer,
    AdminSerializer,
    ChatSerializer,
    ClinicSerializer,
)


class PetcareUserViewSet(viewsets.ViewSet):
    queryset = PetcareUser.objects.all()
    serializer_class = PetcareMemberSerializer

    # def retrieve(self, request, pk=None):
    #     username = request.data.get("username")
    #     password = request.data.get("password")
    #
    #     print(request.user.username)
    #     queryset = Shop.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = PetcareMemberSerializer(user)
    #     return Response(serializer.data)



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def create(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        user = PetcareUser(username=username, is_superuser=False, isShop=True)
        user.set_password(password)
        user.save()
        return super().create(request, *args, **kwargs)

    # def update(self, request, *args, **kwargs):
    #     super().update(request, *args, **kwargs)
    #     # Change password
    #     # Lay id cua thang request, change password cua user
    #     return {"Status": "Done"}


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def create(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        user = PetcareUser(username=username, password=password, is_superuser=False, isCustomer=True)
        user.set_password(password)
        user.save()
        return super().create(request, *args, **kwargs)


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def create(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        user = PetcareUser(username=username, password=password, is_superuser=False, isAdmin=True)
        user.set_password(password)
        user.save()
        return super().create(request, *args, **kwargs)


class ClinicViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["id"] = user.id
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
