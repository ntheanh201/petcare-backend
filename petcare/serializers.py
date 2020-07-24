from rest_framework import serializers
from .models import (
    PetcareUser,
    Product,
    Order,
    Review,
    Sale,
    Shop,
    Chat,
    Customer,
    Admin,
    Cart,
    Clinic,
)


class PetcareMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetcareUser
        # fields = [
        #     "avatar",
        #     "url",
        #     "id",
        #     "username",
        #     "gender",
        #     "fullname",
        #     "phone",
        #     "address",
        #     "email",
        #     "dateOfBirth",
        #     "password"
        # ]
        fields = "__all__"


class ShopSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Shop
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = "__all__"


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
