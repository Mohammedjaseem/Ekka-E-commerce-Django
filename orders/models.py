from django.db import models
from accounts.models import Account
from store.models import Product, Variation

# Create your models here.
class Payment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    amount_paid = models.FloatField() #total ampount paid
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id

class Order(models.Model):
    STATUS = (
        ('new', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    ORDER_STATUS = (
        ('Accepted', 'Accepted'),
        ('Ready to ship', 'Ready to ship'),
        ('On shipping', 'On shipping'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
        ('return', 'return'),
        ('Refunded', 'Refunded'),
    )

    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    order_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    payment_method = models.CharField(max_length=50, blank=True)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100,  blank=True)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    order_note = models.TextField(blank=True)
    order_total = models.FloatField()
    tax = models.FloatField()
    status = models.CharField(max_length=50, choices=STATUS, default='new')
    ip = models.CharField(blank=True, max_length=20)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS, default='Accepted')

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.order_number 

    def full_name (self):
        return self.first_name + ' ' + self.last_name

    def address (self):
        return self.address_line_1 + ' ' + self.address_line_2 + ' ' + self.city + ' ' + self.state + ' ' + self.country
    
    def date (self):
        return self.created_at.strftime('%d %b %Y')

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation = models.ManyToManyField(Variation, blank=True)
    quantity = models.IntegerField()
    product_price = models.FloatField()
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name
