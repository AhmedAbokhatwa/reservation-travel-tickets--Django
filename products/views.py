from django.shortcuts import get_object_or_404 ,render
from .models import Product
# Create your views here.
from django.http import HttpResponse
def hello (request):
  return HttpResponse("hello")

def all_products(request):
  # return HttpResponse("helloo")
  products = Product.objects.all()
  filer_product1 = Product.objects.all().filter(name ='ticket one')
  filer_product2 = products.filter(name ='ticket_cairo')
  order_price = products.order_by('price')
  order_category = products.order_by('category')
  count_product = str(products.count())
  exact_product_name = products.filter(name__exact = "oppo")
  contains_product_name = products.filter(name__contains = "iphon")
  in_product_price = products.filter(price__in = [1500,2500])
  range_product_price = products.filter(price__range= (1500,2500))

  exact_product = products.filter(price__exact = 1500)
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

def pro(request):
  context = Product.objects.all()
  print(context)
  return render(request,'products.pro.html',context)