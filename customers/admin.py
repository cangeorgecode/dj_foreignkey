from django.contrib import admin
from customers.models import Customer, Business

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'name', 'email',]

admin.site.register(Customer, CustomerAdmin)

class BusinessAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Businesses'
    list_display = ['created_at', 'customer', 'address']

admin.site.register(Business, BusinessAdmin)