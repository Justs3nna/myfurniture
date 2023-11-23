from django.db import models
from django.shortcuts import render

class Customer(models.Model):
    customer = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.TextField()
    contact_number = models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'customer'

class Category(models.Model):
    category = models.AutoField(primary_key=True)
    classification = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.classification

    class Meta:
        db_table = 'category'


class Supplier(models.Model):
    supplier = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    contact_number = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'supplier'

class Product(models.Model):
    product = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    specification = models.TextField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    
    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'product'


class Courier(models.Model):
    courier = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = 'courier'

class Transaction(models.Model):
    transaction = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.transaction}"

    class Meta:
        db_table = 'transaction'
    
class Employee(models.Model):
    employee = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'employee'
