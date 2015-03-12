#Python
#Django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import RegexValidator
#Project


# Create your models here.

"""
	Define custom user manager class
"""

class AuthUserManager(BaseUserManager):
	def create_user(self,email,password=None):
		if not email:
			raise ValueError("User must have a valid email address")

		user = self.model(email=self.normalize_email(email),)
		user.is_active = True
		user.set_password(password)
		user.save(using=self.db)
		return user

	def create_superuser(self,email,password):
		user = self.create_user(email=email,password=password)
		user.is_staff = True
		user.is_superuser = True
		user.is_webadmin = True
		user.save(using=self.db)
		return user

"""
	AuthUser for app
"""

class CustomUser(AbstractBaseUser,PermissionsMixin):
	alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allowed.')

	### Redefine the basic fields that would be defined in User ###
	email = models.EmailField(verbose_name='email address', unique=True, max_length=255)
	username = models.CharField(verbose_name='username', max_length=30, blank=True)
	first_name = models.CharField(max_length=30, null=True, blank=True)
	last_name=models.CharField(max_length=50, null=True, blank=True)
	date_joined = models.DateTimeField(auto_now_add=True)
	is_active= models.BooleanField(default=True,null=False)
	is_staff = models.BooleanField(default=False,null=False)
	is_webdirector = models.BooleanField(default=False,null=False)
	is_webmanager = models.BooleanField(default=False,null=False)
	is_webadmin = models.BooleanField(default=False,null=False)


	objects = AuthUserManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	def get_full_name(self):
		fullname = self.first_name +" "+ self.last_name
		return fullname

	def get_short_name(self):
		return self.email

	def __unicode__(self):
		return self.email

