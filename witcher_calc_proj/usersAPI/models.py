from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from witcher_app.utils import unique_slug_generator

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model
    Unique username is requiered but it is not a indetifier for auth
    Email is indetifier and unique field
    first_name, last_name are not requiered fields and can be blank
    objects associates for our CustomUserManager
    """
    username = models.CharField(max_length = 100, unique = True)
    email = models.EmailField(_('Email address'), unique = True)
    first_name = models.CharField(max_length = 150, blank = True)
    last_name = models.CharField(max_length = 150, blank = True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=16)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user:user-detail', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        slug_text = f'{self.username}'        
        self.slug = unique_slug_generator(self, slug_text, self.slug)
        super().save(*args, **kwargs)

