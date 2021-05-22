from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

        def create_user(self, email, password=None, **extract_fields):
            """Creates and saves new user"""
            if not email:
                raise ValueError("user must have email address")
            user = self.model(email=self.normalize_email(email), **extract_fields)
            user.set_password(password)
            user.save(using=self._db)

            return user

        def create_superuser(self,email,passsword):
            """Create super user"""
            user=self.create_user(email,passsword)
            user.is_staff=True
            user.is_superuser=True
            user.save(using=self._db)

            return user
        
class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model class support using email"""
    email =models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)


    objects=UserManager()

    USERNAME_FIELD='email'

     