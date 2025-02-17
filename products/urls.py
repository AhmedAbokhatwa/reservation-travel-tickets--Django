from django.urls import path
from products import views
# yout urlpatens
urlpatterns =[
    #producrs/' '
    path('', views.all_products, name='products'),
    
    path('proc/',views.hello,name='hello'),
    path('<int:pro_id>',views.product,name='product'),
    path('pro/',views.pro,name='pro'),
    
]

