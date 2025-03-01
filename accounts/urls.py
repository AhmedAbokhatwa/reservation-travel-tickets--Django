from django.urls import path
from . import views
from products import views as products

urlpatterns = [
    path('',products.all_products, name='home'),
    path('signin', views.signin , name='signin'),
    path('signup',views.signup, name='signup'),
    path('profile',views.profile, name='profile'),
    path('logout',views.logout, name='logout'),
    path('product_favorites/<int:pro_id>',views.product_favorite, name='product_favorite'),
    path('show_product_favorite',views.show_product_favorite,name='show_product_favorite'),
] 