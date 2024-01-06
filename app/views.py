from django.shortcuts import render

# Create your views here.

def about(request):
   return render(request,'pages/about.html')

def index(request):
   return render(request,'pages/index.html')

def service(request):
   return render(request,'pages/service.html')

def contact(request):
   return render(request,'pages/contact.html')

def blog(request):
   return render(request,'pages/blog.html')   

def destination(request):
   return render(request,'pages/destination.html')   

def single(request):
   return render(request,'pages/single.html')     

def guide(request):
   return render(request,'pages/guide.html')

def testimonial(request):
   return render(request,'pages/testimonial.html')         



