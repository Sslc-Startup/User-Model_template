from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.PositiveIntegerField()
    reorder_level = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order {self.id} - {self.customer.name}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.product.name} x {self.quantity}'

class InventoryMovement(models.Model):
    MOVEMENT_TYPES = [
        ('IN', 'In'),
        ('OUT', 'Out'),
        ('TRANSFER', 'Transfer')
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    movement_type = models.CharField(max_length=50, choices=MOVEMENT_TYPES)
    quantity = models.PositiveIntegerField()
    movement_date = models.DateField()
    reference = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.product.name} {self.movement_type} {self.quantity}'

class Transfer(models.Model):
    source_location = models.CharField(max_length=100)
    destination_location = models.CharField(max_length=100)
    transfer_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f'Transfer from {self.source_location} to {self.destination_location}'

class TransferItem(models.Model):
    transfer = models.ForeignKey(Transfer, on_delete=models.CASCADE, related_name='transfer_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.product.name} x {self.quantity}'

class Location(models.Model):
    location_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.location_name

class ProductLocation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.product.name} at {self.location.location_name}'
