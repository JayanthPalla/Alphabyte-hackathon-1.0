from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from django.contrib.auth.models import BaseUserManager

class ApplicantUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class ApplicantUser(AbstractUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    full_name = models.CharField(max_length=255, verbose_name='full name')
    resume_file_path = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = ApplicantUserManager()
    
    
    def __str__(self) -> str:
        return f'{self.full_name} ({self.email})'
    
    
