from django.contrib.auth.models import User, AbstractUser
from django.db import models
import uuid

from petcare.enums import OrderStatus, Gender, AdminRole, Sender


def custom_media_path(instance, filename):
    file_ext = filename.split(".")[-1]
    return str(uuid.uuid4()) + "." + file_ext


class Image(models.Model):
    img_url = models.FileField(
        upload_to=custom_media_path, max_length=100, default="default.jpg"
    )


# RootAdmin
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
    isAdmin = models.BooleanField(null=False, default=False)
    isShop = models.BooleanField(null=False, default=False)
    isCustomer = models.BooleanField(null=False, default=False)

    def addClinic(self):
        pass

    def editClinic(self):
        pass

    def editAdmin(self):
        pass

    def addAdmin(self):
        pass

    def __str__(self):
        return f"{self.username} - {self.fullname}"


class Shop(models.Model):
    username = models.CharField(max_length=100, default="", unique=True)
    password = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=1000, null=False, blank=False, default="")
    businessLicense = models.TextField(null=True, default="", blank=True)
    avatar = models.FileField(
        upload_to=custom_media_path, max_length=100, default="default.jpg"
    )
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    warehouseAddress = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    ratings = models.FloatField(null=True, blank=True)

    def getAllShop(self):
        return Shop.objects.all()

    def getShopById(self, id):
        return Shop.objects.filter(id=id).first()

    def __str__(self):
        return f"{self.id}: {self.username} - {self.name}"


class Customer(models.Model):
    username = models.CharField(max_length=100, default="", unique=True)
    password = models.CharField(max_length=100, default="")
    avatar = models.FileField(
        upload_to=custom_media_path, max_length=100, default="default.jpg"
    )
    name = models.CharField(max_length=1000, null=False, blank=False, default="")
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

    def getInfo(self):
        return f"{self.username} - {self.name} - {self.gender} - {self.fullname} - {self.phone} - " \
               f"{self.address} - {self.email} - {self.dateOfBirth} "

    def saveInfo(self):
        # save info of customer from form
        pass

    def __str__(self):
        return f"{self.id}: {self.username} - {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=1000, null=False, blank=False)
    price = models.FloatField(null=False)
    amount = models.IntegerField(null=False)
    productType = models.CharField(max_length=1024, null=False, blank=False)
    productImage = models.FileField(
        upload_to=custom_media_path, max_length=100, default="default.jpg"
    )
    isApproval = models.BooleanField(default=False, null=False)
    buyAmount = models.IntegerField(null=False, default=0)
    shopId = models.ForeignKey(
        Shop, on_delete=models.CASCADE, null=True, default=None, blank=True,
    )
    description = models.TextField(null=True, blank=True)

    def checkApproval(self):
        if self.isApproval:
            return "Approved"
        return "Not Approved"

    def __str__(self):
        return f"{self.name} - {self.checkApproval()}"


class Cart(models.Model):
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False, default=1)
    customerId = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key=True, default=None
    )
    productId = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, default=None, blank=True,
    )

    def __str__(self):
        return f"{self.customerId.username} - {self.productId.name}"


class Admin(models.Model):
    username = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=1000, null=False, blank=False, default="")
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
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    dateOfBirth = models.CharField(max_length=100, null=True, blank=True)
    role = models.SmallIntegerField(
        null=False,
        blank=False,
        choices=[
            (AdminRole.LEVEL1.value, AdminRole.LEVEL1.name),
            (AdminRole.LEVEL2.value, AdminRole.LEVEL2.name),
        ],
        default=AdminRole.LEVEL1.value,
    )
    shops = models.ManyToManyField(Shop, null=True, blank=True, default=None)
    customers = models.ManyToManyField(Customer, null=True, blank=True, default=None)
    products = models.ManyToManyField(Product, null=True, blank=True, default=None)

    def checkRole(self):
        if self.role == AdminRole.LEVEL1.value:
            return "Level 1"
        if self.role == AdminRole.LEVEL2.value:
            return "Level 2"

    def updateRole(self, id, role):
        admin = Admin.objects.filter(id=id).first()
        if role == AdminRole.LEVEL1.value:
            admin.role = AdminRole.LEVEL1.value
        if role == AdminRole.LEVEL2.value:
            admin.role = AdminRole.LEVEL2.value
        admin.save()

    def addAdmin(self):
        # add admin from form
        pass

    def deleteAdmin(self, id):
        # delete admin
        pass

    def saveAdminInfo(self):
        # get user info from forms
        pass

    def __str__(self):
        return f"{self.id}: {self.username} - {self.name} - {self.checkRole()}"


class Clinic(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.FileField(
        upload_to=custom_media_path, max_length=100, default="default.jpg"
    )
    address = models.CharField(max_length=100, null=True, blank=True)
    specialist = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default="")

    def getName(self):
        return self.name

    def deleteClinic(self, id):
        # delete clinic by id
        pass

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(null=False)
    amount = models.IntegerField(null=False)
    deliveryOn = models.DateTimeField(null=True, blank=True)
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
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    customerId = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, default=None, blank=True,
    )
    productId = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, default=None, blank=True,
    )
    shopId = models.ForeignKey(
        Shop, on_delete=models.CASCADE, null=True, default=None, blank=True,
    )

    def createOrder(self):
        # create an order
        pass

    def __str__(self):
        return f"{self.customerId.username} - {self.productId.name}"


class Review(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(null=False, default=0)
    reviewContent = models.CharField(max_length=1000, null=True, blank=True)
    customerId = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, default=None, blank=True,
    )
    shopId = models.ForeignKey(
        Shop, on_delete=models.CASCADE, null=True, default=None, blank=True,
    )

    def __str__(self):
        return f"{self.customerId.username} - {self.shopId.username} - {self.rating}"


class Sale(models.Model):
    name = models.CharField(max_length=1024, null=False, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    salePrice = models.FloatField(null=False)
    shopId = models.ForeignKey(
        Shop, on_delete=models.SET_NULL, null=True, default=None, blank=True,
    )

    def getShopName(self):
        return self.shopId.name

    def __str__(self):
        return f"{self.name} - {self.getShopName()}"


class Message(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    sender = models.SmallIntegerField(
        null=False,
        blank=False,
        choices=[
            (Sender.CUSTOMER.value, Sender.CUSTOMER.name),
            (Sender.SHOP.value, Sender.SHOP.name),
        ],
        default=Sender.CUSTOMER.value,
    )
    senderId = models.IntegerField(null=False, blank=False, default=0)
    content = models.TextField(default="")

    def __str__(self):
        return f"{self.content}"


class Chat(models.Model):
    shopId = models.ForeignKey(
        Shop, on_delete=models.CASCADE, null=False, default=None, blank=False,
    )
    customerId = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=False, default=None, blank=False,
    )
    messages = models.ForeignKey(
        Message, on_delete=models.CASCADE, null=False, default=None, blank=False,
    )

    def __str__(self):
        return f"{self.shopId.username} - {self.customerId}: {self.messages}"
