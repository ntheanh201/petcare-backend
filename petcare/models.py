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

    # software = models.SmallIntegerField(
    #     null=False,
    #     blank=False,
    #     choices=[
    #         (SellerSoftware.HARAVAN.value, SellerSoftware.HARAVAN.name),
    #         (SellerSoftware.MSHOP_KEEPER.value, SellerSoftware.MSHOP_KEEPER.name),
    #         (SellerSoftware.KIOT_VIET.value, SellerSoftware.KIOT_VIET.name),
    #         (SellerSoftware.UNKNOWN.value, SellerSoftware.UNKNOWN.name),
    #     ],
    #     default=SellerSoftware.UNKNOWN.value,
    # )
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    userId = models.ForeignKey(PetcareUser, on_delete=models.CASCADE, null=True, default=None)
    businessLicense = models.TextField()
    address = models.CharField(max_length=1024, null=False, blank=False, default="")
    phoneNumber = models.CharField(max_length=17, blank=True)

    def get_mail(self):
        if self.userId is not None:
            return self.userId.email
        return "unknown"

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def __str__(self):
        if self.userId is not None:
            return f"{self.get_id()}-{self.get_name()}-{self.get_mail()}"


# class Customer(models.Model):
#     first_name = models.CharField(max_length=1024, null=False, blank=False, default="")
#     last_name = models.CharField(max_length=1024, null=False, blank=False, default="")
#     email = models.EmailField(max_length=254, null=False)
#     address = models.CharField(max_length=1024, null=False, blank=False, default="")
#     phone_number = models.CharField(max_length=17, blank=True)
#
#     # A json string used to store dynamic data such as tokens, secrets...
#     extra_data = models.TextField(null=False, blank=True, default="")
#
#     @property
#     def extra_data_as_dict(self) -> Dict:
#         return json.loads(self.extra_data)
#
#     def get_extra_data_field(self, key: str):
#         extra_data = self.extra_data_as_dict
#         if key not in extra_data:
#             raise Exception(f"{key} not found in extra_data for {self}")
#         return extra_data[key]
#
#     def get_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     def __str__(self):
#         return f"{self.id}-{self.get_name()}-{self.email}"


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
        Shop, on_delete=models.SET_NULL, null=True, default=None, blank=True,
    )


class Order(models.Model):
    name = models.CharField(max_length=1000, null=False, blank=False)
    price = models.FloatField(null=False)
    amount = models.IntegerField(null=False)

    userId = models.ForeignKey(
        PetcareUser, on_delete=models.SET_NULL, null=True, default=None, blank=True,
    )
    productId = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, default=None, blank=True,
    )
    createdAt = models.DateTimeField(auto_now_add=True)
    deliveriedOn = models.DateTimeField(null=True, blank=True)
    averageRating = models.IntegerField(null=True, blank=True)
    categories = ArrayField(ArrayField(models.IntegerField()))
    imageURL = models.FileField(
        upload_to=custom_media_path, max_length=100, default="default.jpg"
    )
    longDescription = models.TextField(null=True, blank=True)
    shortDescription = models.TextField(null=True, blank=True)
    extra_data = models.TextField(blank=True, null=False, default="{}")

    def extra_data_dict(self) -> Dict:
        if self.extra_data is None or len(self.extra_data) == 0:
            return {}
        return json.loads(self.extra_data)


class Review(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    productName = models.CharField(max_length=100, null=False, blank=False)
    rating = models.IntegerField(null=True)
    reviewContent = models.CharField(max_length=1000, null=True, blank=True)
    productImage = models.FileField(
        upload_to=custom_media_path, max_length=100, default="default.jpg"
    )
    productPrice = models.FloatField(null=False)
    productType = models.CharField(max_length=100, null=False, blank=False)


class Sale(models.Model):
    name = models.CharField(max_length=1024, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    salePrice = models.FloatField(null=False)
