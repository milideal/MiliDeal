
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# from djongo import models
# from djongo.models import DjongoManager
# class UserManager(DjongoManager):


class UserManager(BaseUserManager):
    use_in_migrations = True

    # Email 중복 확인 메서드
    def email_exists(self, email: str):
        users = User.objects.all()
        user = users.objects.filter(email=email).first()
        if user:
            return True
        else:
            return False

    def create_user(self, email, password=None, nickname=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)

        user = self.model(email=email, nickname=nickname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, nickname=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, nickname, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    # username = models.TextField(max_length=30, unique=True)
    email = models.EmailField(unique=True, primary_key=True)
    nickname = models.CharField(max_length=30, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        """
        Save the user with lowercase email.
        """
        self.email = self.email.lower()
        super(User, self).save(*args, **kwargs)

    class Meta:
        app_label = 'user'
        db_table = "users"
        # ordering = ['slug']
