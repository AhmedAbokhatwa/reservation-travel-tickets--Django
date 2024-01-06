from django.urls import path
from . import views

urlpatterns = [
     path('', views.index , name='index'),
     path('about',views.about, name='about'),
     path('service',views.service, name='service'),
     path('contact',views.contact, name='contact'),
     path('blog',views.blog, name='blog'),
     path('destination',views.destination, name='destination'),
     path('single',views.single, name='single'),
     path('guide',views.guide, name='guide'),
     path('testimonial',views.testimonial, name='testimonial'),
]
