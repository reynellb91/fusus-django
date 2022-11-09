import uuid

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


# Create your models here.
class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=16, null=True, blank=True)
    address = models.CharField(max_length=1024, null=True, blank=True)

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    # https://koenwoortman.com/python-django-email-as-username/
    REQUIRED_FIELDS = []
    USERNAME_FIELD: str = "email"

    username = None

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=16, null=True, blank=True)
    email = models.EmailField(unique=True)
    organization = models.ForeignKey(to=Organization, on_delete=models.CASCADE, related_name="users", null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    objects = UserManager()





