from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, name,email,mobile_number,password=None):
        if not email:
            raise ValueError("users must have an email address. ")
        if not mobile_number:
            raise ValueError("users must have a mobile number. ")
        
        user = self.model(
            email = self.normalize_email(email),
            name = name,
            mobile_number = mobile_number,
        )
        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_superuser(self, name, email, mobile_number, role, password=None):
        user = self.model(
            email = self.normalize_email(email),
            name = name,
            mobile_number = mobile_number,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self.db)
        return user


class User(AbstractBaseUser):
    
    name                = models.CharField(max_length=250)
    email               = models.EmailField(unique=True)
    mobile_number       = models.CharField(max_length=250,unique=True)
    date_joined         = models.DateField(auto_now_add=True)
    last_login          = models.DateField(auto_now=True)
    is_active           = models.BooleanField(default=True)
    is_superuser        = models.BooleanField(default=False)
    is_admin            = models.BooleanField(default=False)
    is_staff            = models.BooleanField(default=False)

    USERNAME_FIELD      = 'email'
    REQUIRED_FIELDS      = ['mobile_number','name']

    objects = MyAccountManager()

    def _str_(self):
        return self.name +'/' + self.email
    
    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True



class DropBox(models.Model):
    title = models.CharField(max_length=30)
    document = models.FileField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
        verbose_name_plural = 'Drop Boxes'