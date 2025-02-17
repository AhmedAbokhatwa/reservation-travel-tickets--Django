from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    choices = [
        ('Cairo','Cairo'),
        ('Alexandria','Alexandria'),
        ('Tanta','Tanta')
    ]
    name = models.CharField(max_length =50 , verbose_name='Title')
    description = models.TextField(default= 'put your text',blank= True, null= True)
    price =models.DecimalField( max_digits=6 , decimal_places=2 )
    photo = models.ImageField(upload_to='photos/%y/%m%d', verbose_name='photo',default= 'photos/2023/1230/package-1.jpg')
    person = models.ForeignKey(User, on_delete=models.CASCADE)  
    is_active = models.BooleanField(default=True)
    published_date = models.DateTimeField(default=datetime.now)
    category = models.CharField(max_length=50,choices= choices)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'products NAME'
        ordering =['-price']  

class Category(models.Model):
      published_date = models.DateTimeField(default=datetime.now)
      name = models.CharField(max_length=50, verbose_name='Category Name')
      def __str__(self):
        return self.name
      class Meta:
        verbose_name = 'Category NAME'
        ordering =['name']  
