from django.contrib import admin
from django.contrib.auth.hashers import make_password

from .models import (
    PetcareUser,
    Sale,
    Shop,
    Product,
    Order,
    Review,
    Customer,
    Admin,
    Cart,
    Clinic,
    Chat,
)


class ProductAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class ShopAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = PetcareUser(username=username, is_superuser=False, isShop=True)
        user.set_password(password)
        user.save()

        obj.password = make_password(password)
        obj.save()
        super().save_model(request, obj, form, change)


class CustomerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = PetcareUser(username=username, is_superuser=False, isCustomer=True)
        user.set_password(password)
        user.save()

        obj.password = make_password(password)
        obj.save()
        super().save_model(request, obj, form, change)


class NormalAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = PetcareUser(username=username, is_superuser=False, isAdmin=True)
        user.set_password(password)
        user.save()

        obj.password = make_password(password)
        obj.save()
        super().save_model(request, obj, form, change)


admin.site.site_header = "PetCare RootAdmin"
admin.site.register(PetcareUser)
admin.site.register(Sale)
admin.site.register(Cart)
admin.site.register(Clinic)
# admin.site.register(Chat)
admin.site.register(Admin, NormalAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Review)
