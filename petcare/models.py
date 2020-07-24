import json
from typing import Dict

from django.contrib.auth.models import User, AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.conf import settings
import uuid

from petcare.enums import OrderStatus, Gender


def custom_media_path(instance, filename):
    file_ext = filename.split(".")[-1]
    return str(uuid.uuid4()) + "." + file_ext


class Image(models.Model):
    img_url = models.FileField(
        upload_to=custom_media_path, max_length=100, default="default.jpg"
    )


class PetcareUser(AbstractUser):
    avatar = models.FileField(
        upload_to=custom_media_path, max_length=100, default="default.jpg"
    )
    gender = models.CharField(max_length=15, null=True, blank=True)
    fullname = models.CharField(max_length=1024, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    dateOfBirth = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "user: {}".format(self.username)


class Shop(models.Model):
    username = models.CharField(max_length=100, default="", unique=True)
    password = models.CharField(max_length=32, default="")
    businessLicense = models.TextField()
    avatar = models.FileField(
        upload_to=custom_media_path, max_length=100, default="default.jpg"
    )
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    warehouseAddress = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    ratings = models.FloatField(null=True, blank=True)
    isVip = models.BooleanField(null=False, default=False)
    vipExpires = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.username}"


class Customer(models.Model):
    username = models.CharField(max_length=100, default="", unique=True)
    password = models.CharField(max_length=32, default="")
    avatar = models.FileField(
        upload_to=custom_media_path, max_length=100, default="default.jpg"
    )
    gender = models.SmallIntegerField(
        null=False,
        blank=False,
        choices=[
            (Gender.MALE.value, Gender.MALE.name),
            (Gender.FEMALE.value, Gender.FEMALE.name),
            (Gender.UNDEFINED.value, Gender.UNDEFINED.name),
        ],
        default=Gender.UNDEFINED.value,
    )
    fullname = models.CharField(max_length=1024, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    dateOfBirth = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.username}"


class Product(models.Model):
    name = models.CharField(max_length=1000, null=False, blank=False)
    price = models.FloatField(null=False)
    amount = models.IntegerField(null=False)
    productType = models.CharField(max_length=1024, null=False, blank=False)
    rate = models.FloatField(null=False)
    productImage = models.FileField(
        upload_to=custom_media_path, max_length=100, default="default.jpg"
    )
    isApproval = models.BooleanField(default=False, null=False)
    buyAmount = models.IntegerField(null=False, default=0)
    shopId = models.ForeignKey(
        Shop, on_delete=models.CASCADE, null=True, default=None, blank=True,
    )

    def __str__(self):
        return f"{self.name}"


class Cart(models.Model):
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False, default=1)
    userId = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=False, default=None, blank=False,
    )
    productId = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, default=None, blank=True,
    )

    def __str__(self):
        return f"{self.userId.username} - {self.productId.name}"


class Admin(models.Model):
    username = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=32, default="")
    avatar = models.FileField(
        upload_to=custom_media_path, max_length=100, default="default.jpg"
    )
    gender = models.SmallIntegerField(
        null=False,
        blank=False,
        choices=[
            (Gender.MALE.value, Gender.MALE.name),
            (Gender.FEMALE.value, Gender.FEMALE.name),
            (Gender.UNDEFINED.value, Gender.UNDEFINED.name),
        ],
        default=Gender.UNDEFINED.value,
    )
    fullname = models.CharField(max_length=1024, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    dateOfBirth = models.CharField(max_length=100, null=True, blank=True)
    role = models.IntegerField(default=1, null=False, blank=False)
    shops = models.ManyToManyField(Shop, null=True, blank=True, default=None)
    customers = models.ManyToManyField(Customer, null=True, blank=True, default=None)
    products = models.ManyToManyField(Product, null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.username}"


class Clinic(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.FileField(
        upload_to=custom_media_path, max_length=100, default="default.jpg"
    )
    address = models.CharField(max_length=100, null=True, blank=True)
    specialist = models.CharField(max_length=100, null=True, blank=True)
    data = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(null=False)
    amount = models.IntegerField(null=False)
    deliveriedOn = models.DateTimeField(null=True, blank=True)
    imageURL = models.FileField(
        upload_to=custom_media_path, max_length=100, default="default.jpg"
    )
    status = models.SmallIntegerField(
        null=False,
        blank=False,
        choices=[
            (OrderStatus.CHECKING.value, OrderStatus.CHECKING.name),
            (OrderStatus.SHIPPING.value, OrderStatus.SHIPPING.name),
            (OrderStatus.DONE.value, OrderStatus.DONE.name),
            (OrderStatus.CANCEL.value, OrderStatus.CANCEL.name),
        ],
        default=OrderStatus.CHECKING.value,
    )
    longDescription = models.TextField(null=True, blank=True)
    shortDescription = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    extra_data = models.TextField(blank=True, null=False, default="{}")
    userId = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, default=None, blank=True,
    )
    productId = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, default=None, blank=True,
    )
    shopId = models.ForeignKey(
        Shop, on_delete=models.CASCADE, null=True, default=None, blank=True,
    )

    def __str__(self):
        return f"{self.userId.username} - {self.productId.name}"

    def extra_data_dict(self) -> Dict:
        if self.extra_data is None or len(self.extra_data) == 0:
            return {}
        return json.loads(self.extra_data)


class Review(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(null=False, default=0)
    reviewContent = models.CharField(max_length=1000, null=True, blank=True)
    userId = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, default=None, blank=True,
    )
    shopId = models.ForeignKey(
        Shop, on_delete=models.CASCADE, null=True, default=None, blank=True,
    )

    def __str__(self):
        return f"{self.userId.username} - {self.shopId.username} - {self.rating}"


class Sale(models.Model):
    name = models.CharField(max_length=1024, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    salePrice = models.FloatField(null=False)
    shopId = models.ForeignKey(
        Shop, on_delete=models.SET_NULL, null=True, default=None, blank=True,
    )

    def __str__(self):
        return f"{self.name}"


class Chat(models.Model):
    shopId = models.ForeignKey(
        Shop, on_delete=models.CASCADE, null=False, default=None, blank=False,
    )
    userId = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=False, default=None, blank=False,
    )
    content = models.TextField(null=False, blank=False)

    def __str__(self):
        return f"{self.shopId.username} - {self.userId}: {self.content}"
