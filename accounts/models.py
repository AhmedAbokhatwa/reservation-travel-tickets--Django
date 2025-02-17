from django.db import models
from django.contrib.auth.models import User,BaseUserManager
from products.models import Product
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    product_favorites =models.ManyToManyField(Product,default= 'put your text',blank= True, null= True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_number = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username       
    class Meta:
        verbose_name = 'Pofile for user sign in'
        ordering = ['user']



class AccountManager(BaseUserManager):
  use_in_migrations = True

  def _create_user(self, email, name, phone, password, **extra_fields):

      values = [email, name, phone]
      field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))

      for field_name, value in field_value_map.items():
          if not value:
              raise ValueError('The {} value must be set'.format(field_name))

      email = self.normalize_email(email)

      user = self.model(
          email=email,
          name=name,
          phone=phone,
          **extra_fields
      )

      user.set_password(password)
      user.save(using=self._db)

      return user

  def create_user(self, email, name, phone, password=None, **extra_fields):
      extra_fields.setdefault('is_staff', False)
      extra_fields.setdefault('is_superuser', False)
      return self._create_user(email, name, phone, password, **extra_fields)

  def create_superuser(self, email, name, phone, password=None, **extra_fields):
      extra_fields.setdefault('is_staff', True)
      extra_fields.setdefault('is_superuser', True)

      if extra_fields.get('is_staff') is not True:
          raise ValueError('Superuser must have is_staff=True.')
      if extra_fields.get('is_superuser') is not True:
          raise ValueError('Superuser must have is_superuser=True.')
      
      return self._create_user(email, name, phone, password, **extra_fields)
