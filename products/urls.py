from django.urls import path
from . import views
# yout urlpatens

urlpatterns =[
    path('products',views.products,name='products'),
    path('<int:pro_id>',views.product,name='product'),
    
]