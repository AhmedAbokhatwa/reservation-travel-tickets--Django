from django.urls import path
from products import views
# yout urlpatens
urlpatterns =[
    path('', views.all_products, name='products'),
    path('pro/',views.hello,name='hello'),
    path('<int:pro_id>',views.product,name='product'),
    
]

