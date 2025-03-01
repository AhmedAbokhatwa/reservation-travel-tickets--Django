from django.urls import path,include
from products import views
# yout urlpatens
urlpatterns =[
    path('', views.all_products, name='products'),
    path('product/<int:pro_id>',views.product,name='product'),
    
]

