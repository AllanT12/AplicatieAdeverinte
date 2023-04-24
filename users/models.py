from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.db import models
from django.dispatch import receiver


# Create your models here.
class Users(AbstractUser):
    STUDENT = 0
    SECRETARA = 1
    ADMIN = 2
    ROLES = (
        (STUDENT, "STUDENT"),
        (SECRETARA, "SECRETARA"),
        (ADMIN, "ADMIN"),
    )
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    role = models.IntegerField(choices=ROLES, default=STUDENT)
    is_active = models.BooleanField(default=True)
    specializare = models.ManyToManyField('specializari.Specializari')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'password']



