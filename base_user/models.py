from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=256)
    profile_photo = models.ImageField(upload_to='profile_photo/',default='static/images/pp.jpeg')
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Friends(models.Model):
    
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE,related_name='user_owner')
    friend = models.ForeignKey('CustomUser', on_delete=models.CASCADE,related_name='user_friends')
    is_accapted = models.BooleanField(default=False)


class BlockedList(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE,related_name='user')
    blocked_user = models.ForeignKey('CustomUser', on_delete=models.CASCADE,related_name='blocked_user')
    