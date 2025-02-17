from django.shortcuts import get_object_or_404 ,render
from .models import Product
# Create your views here.
from django.http import HttpResponse
def hello (request):
  return HttpResponse("hello")

def all_products(request):
  # return HttpResponse("helloo")
  products = Product.objects.all()
  print("\n\nContext: ", products)
  context ={
     'products': products
  }
  # print("\n\nContext")
  return render(request,'products/products.html',context)

def product(request,pro_id):
  context ={
     'pro': get_object_or_404(product, pk=pro_id),
  }
  return render(request,'products/product.html',context)