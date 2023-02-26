from django.db import models

# Create your models here.

class CustomerInfo(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=170)
    address = models.CharField(max_length=150)
    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Client {str(self.client_id).zfill(8)} - {self.email}"
    

class CustomerPreview(models.Model):
    order = models.CharField(max_length=100)
    transaction = models.CharField(max_length=100)
    initial_amount = models.CharField(max_length=100)
    total_charges = models.CharField(max_length=100)
    payment_reference = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.order}"
    
