from email.policy import default
from tkinter import CASCADE
from django.db import models
from authentication.models import User
# Create your models here.
class Order(models.Model):
    SIZES=(
        ('SMALL','small'),
        ('MEDIUM','medium'),
        ("LARGE",'large'),
        ('EXTRA_LARGE','extralarge')
    )
    ORDER_STATUS=(
        ('PENDING','pending'),
        ('IN_TRANSIT','inTransit'),
        ('DELIVERD','delivered')
    )

    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    size=models.CharField(max_length=20,choices=SIZES,default=SIZES[0][0])
    order_status=models.CharField(max_length=20,choices=ORDER_STATUS,default=ORDER_STATUS[0][0])
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Order {self.size} by {self.customer.id}"