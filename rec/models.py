from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin 

class RecruiterUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class RecruiterUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    full_name = models.CharField(max_length=255, verbose_name='full name')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = RecruiterUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.full_name} ({self.email})'
    
    
    # def has_perm(self, perm, obj=None):
    #     return self.is_staff

    # def has_module_perms(self, app_label):
    #     return self.is_staff
