from django.db import models

class Customer(models.Model):
    created_at = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.name
    
class Business(models.Model):
    created_at = models.DateField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='biz')
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.customer.name