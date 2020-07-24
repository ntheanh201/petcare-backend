import json
from typing import Dict

from django.contrib.auth.models import User, AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.conf import settings
import uuid


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
    username = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=32, default="")
    businessLicense = models.TextField()
    avatar = models.FileField(
        upload_to=custom_media_path, max_length=100, default="default.jpg"
    )
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    ratings = models.FloatField(null=True, blank=True)


class Customer(models.Model):
    username = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=32, default="")
    avatar = models.FileField(
        upload_to=custom_media_path, max_length=100, default="default.jpg"
    )
    gender = models.CharField(max_length=15, null=True, blank=True)
    fullname = models.CharField(max_length=1024, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    dateOfBirth = models.CharField(max_length=100, null=True, blank=True)


class Cart(models.Model):
    name = models.CharField(max_length=1024, null=False, blank=False)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False, default=1)
    userId = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=False, default=None, blank=False,
    )


class Product(models.Model):
    name = models.CharField(max_length=1000, null=False, blank=False)
    price = models.FloatField(null=False)
    amount = models.IntegerField(null=False)
    productType = models.CharField(max_length=1024, null=False, blank=False)
    rate = models.FloatField(null=False)
    productImage = models.FileField(
        upload_to=custom_media_path, max_length=100, default="default.jpg"
    )
    buyAmount = models.IntegerField(null=False, default=0)
    shopId = models.ForeignKey(
        Shop, on_delete=models.CASCADE, null=True, default=None, blank=True,
    )
    carts = models.ManyToManyField(Cart)


class Admin(models.Model):
    username = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=32, default="")
    avatar = models.FileField(
        upload_to=custom_media_path, max_length=100, default="default.jpg"
    )
    gender = models.CharField(max_length=15, null=True, blank=True)
    fullname = models.CharField(max_length=1024, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    dateOfBirth = models.CharField(max_length=100, null=True, blank=True)
    role = models.IntegerField(default=1, null=False, blank=False)
    shops = models.ManyToManyField(Shop)
    customers = models.ManyToManyField(Customer)
    products = models.ManyToManyField(Product)


class Clinic(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.FileField(
        upload_to=custom_media_path, max_length=100, default="default.jpg"
    )
    address = models.CharField(max_length=100, null=True, blank=True)
    specialist = models.CharField(max_length=100, null=True, blank=True)
    data = models.TextField()


class Order(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=1000, null=False, blank=False)
    price = models.FloatField(null=False)
    amount = models.IntegerField(null=False)
    deliveriedOn = models.DateTimeField(null=True, blank=True)
    imageURL = models.FileField(
        upload_to=custom_media_path, max_length=100, default="default.jpg"
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


class Sale(models.Model):
    name = models.CharField(max_length=1024, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    salePrice = models.FloatField(null=False)
    shopId = models.ForeignKey(
        Shop, on_delete=models.SET_NULL, null=True, default=None, blank=True,
    )


class Chat(models.Model):
    shopId = models.ForeignKey(
        Shop, on_delete=models.CASCADE, null=False, default=None, blank=False,
    )
    userId = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=False, default=None, blank=False,
    )
    content = models.TextField(null=False, blank=False)
