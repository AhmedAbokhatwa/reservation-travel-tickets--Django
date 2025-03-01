from django.shortcuts import get_object_or_404 ,render
from .models import Product
# Create your views here.
from django.http import HttpResponse
def hello (request):
  return HttpResponse("hello")

def all_products(request):
  try:
    products = Product.objects.all()
    context ={
     'products': products
  }
  except Product.DoesNotExist:
      html_response = '<h3>page not found</h3>'
      return HttpResponse(html_response)
  return render(request,'products/products.html',context)

def product(request,pro_id):
  context ={
     'pro': Product.objects.get(pk=pro_id),
  }
  print("\\n\ncontexxxt",context)
  # context ={
  #    'pro': get_object_or_404(product, pk=pro_id),
  # }
  return render(request,'products/product.html',context)

def pro(request):
  context = Product.objects.all()
  print(context)
  return render(request,'products.pro.html',context)