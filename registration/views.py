from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Customer, Employee, Transaction, Courier
from django.http import JsonResponse
from datetime import datetime

def signup(request):
    if request.method == 'POST':
        # Retrieve form data using request.POST.get() method
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact_number = request.POST.get('contact_number')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if any required field is empty
        if not name or not address or not contact_number or not username or not password:
            messages.error(request, 'Please fill in all the fields.')
            return redirect('signup')

        # Check if the contact number exceeds a limit (e.g., 10 digits)
        if len(contact_number) > 13:
            messages.error(request, 'Contact number is too long.')
            return redirect('signup')

        # Check if the username already exists
        if Customer.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')
            return redirect('signup')

        # Create a new customer object and save it to the database
        customer = Customer(name=name, address=address, contact_number=contact_number, username=username,
                            password=password)
        customer.save()
        messages.success(request, 'Sign up successful. Please log in.')
        return redirect('signup')
    else:
        return render(request, 'signup.html')


def cuslogin(request):
    products = Product.objects.all()
    return render(request, 'cuslogin.html', {'products': products})


def index(request):
    product = Product.objects.all()
    return render(request, 'index.html', {'product': product})

def insertproduct(request):
    if request.method == "POST":
        prod = Product ()
        prod.product_name= request.POST.get('product_name')
        prod.price= request.POST.get('price')
        prod.specification = request.POST.get('specification')
        prod.category_id = request.POST.get('category_id')
        prod.supplier_id = request.POST.get('supplier_id')

        if len(request.FILES)!=0:
            prod.image = request.FILES.get('image')

        prod.save()
        messages.success(request, "Product Added Successfully!")

    return render(request, 'insert.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            messages.error(request, 'Please enter your username and password.')
            return redirect('login')

        customer = Customer.objects.filter(username=username).first()
        employee = Employee.objects.filter(username=username).first()

        if customer is not None:
            if customer.password == password:
                return redirect('cuslogin')
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect('login')
        if employee is not None:
            if employee.password == password:
                return redirect('index')
            else:
               messages.error(request, 'Invalid username or password.')
               return redirect('login')

    return render(request, 'signup.html')

def edit(request, product):
    prod = Product.objects.get(product=product)
    return render(request, 'edit.html',{'prod': prod})

def editprod(request, product):
    prod_name = request.POST.get('product_name')
    prod_price = request.POST.get('price')
    prod_specification= request.POST.get('specification')
    prod_category_id = request.POST.get('category_id')
    prod_supplier_id = request.POST.get('supplier_id')
    prod = Product.objects.get(product=product)
    prod.product_name= prod_name
    prod.price = prod_price
    prod.specification = prod_specification
    prod.category_id = prod_category_id
    prod.supplier_id = prod_supplier_id
    prod.save()
    return redirect("index")
    
def delete(request, product):
    prod = Product.objects.get(product=product)
    prod.delete()
    messages.success(request, "Product Deleted Successfully!")
    return redirect("index")

def openCheckoutModal(request, product, prod_price, product_specification, product_supplier_id):
    product = Product.objects.get(product=product)
    product.price = prod_price
    product.specification = product_specification
    product.supplier_id = product_supplier_id
    return render(request, 'cuslogin.html', {'product': product})

def transaction(request):
    # Retrieve the transaction data from the database
    transactions = Transaction.objects.all()

    # Pass the transactions to the template context
    context = {
        'transactions': transactions
    }

    return render(request, 'transaction.html', context)

def submit_order(request):
    if request.method == 'POST':
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        product_id = request.POST.get('product_id')
        courier_id = request.POST.get('courier_id')
        date = datetime.now()  # Use the current date and time

        # Retrieve the related objects
        product = Product.objects.get(id=product_id)
        customer = Customer.objects.get(username=request.user.username)  # Assuming username is used for authentication
        courier = Courier.objects.get(id=courier_id)

        # Calculate the total amount    
        total_amount = float(price) * int(quantity)

        # Create a new transaction object and save it to the database
        transaction = Transaction(
            quantity=quantity,
            total_amount=total_amount,
            date=date,
            courier=courier,
            customer=customer,
            product=product,
        )
        transaction.save()

        # Redirect to the transaction page after successful submission
        return redirect('transaction')
    else:
        # Return a JSON response indicating the failure of the order submission
        return JsonResponse({'success': False})

def tables(request):
    products = Product.objects.filter(category=1)
    return render(request, 'tables.html', {'products': products})

def beds(request):
    products = Product.objects.filter(category=2)
    return render(request, 'beds.html', {'products': products})

def chairs(request):
    products = Product.objects.filter(category=3)
    return render(request, 'chairs.html', {'products': products})

def cabinets(request):
    products = Product.objects.filter(category=4)
    return render(request, 'cabinets.html', {'products': products})

def budget1(request):
    products = Product.objects.all
    return render(request, 'budget1.html', {'products': products})

def budget2(request):
    products = Product.objects.all
    return render(request, 'budget2.html', {'products': products})

def budget3(request):
    products = Product.objects.all
    return render(request, 'budget2.html', {'products': products})