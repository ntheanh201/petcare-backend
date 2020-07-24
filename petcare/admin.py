from django.contrib import admin
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

admin.site.register(PetcareUser)
admin.site.register(Sale)
admin.site.register(Customer)
admin.site.register(Admin)
admin.site.register(Cart)
admin.site.register(Clinic)
admin.site.register(Chat)
admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Review)
