from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Book, Order, Tag


# Create your views here.



def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    context = {'customers': customers, 'orders': orders}
    return render(request,'bookstore/dashboard.html',context)

def books(request):
    books = Book.objects.all()
    return render(request, 'bookstore/books.html', {'books': books})

from django.shortcuts import get_object_or_404

def customer(request, pk):
    customer_obj = get_object_or_404(Customer, id=pk)
    return render(request, 'bookstore/customer.html', {'customer': customer_obj})



# def customer(request, pk):
#     customer_obj = Customer.objects.get(id=pk)
#     return render(request, 'bookstore/customer.html', {'customer': customer_obj})

# def customer(request):
#     return render(request,'bookstore/customer.html')

def testing(request):
    return render(request,'bookstore/testing.html')