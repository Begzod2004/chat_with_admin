# from django.db import models
# from django.contrib.auth.models import BaseUserManager
# from django.conf import settings
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import BaseUserManager
# from django.contrib.auth.models import Group
# from django.contrib.auth.models import Permission



# class UserManager(BaseUserManager):
#     """Manager for users."""

#     def create_user(self, email, password=None, **extra_fields):
#         """Create, save and return a new user."""
#         if not email:
#             raise ValueError('User must have an email address.')
#         user = self.model(email=self.normalize_email(email), **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)

#         return user

#     def create_superuser(self, email, password, **extra_fields):
#         """Create and return a new superuser."""
#         extra_fields.setdefault('is_staff', True)   
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)

# class User(AbstractUser):
#     USER_TYPE_CHOICES = (
#         ('admin', 'Admin'),
#         ('userss', 'Userss')
#     )

#     user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=20)
#     phone_number = models.CharField(max_length=20)
#     chats_sent = models.ManyToManyField('Chat', related_name="chat_sent")
#     chats_received = models.ManyToManyField('Chat', related_name="chat_received")
#     full_name = models.CharField(max_length=255)
#     username = models.CharField(max_length=255, unique=True)
#     objects = UserManager()
#     groups = models.ManyToManyField(Group, blank=True,related_name='home_users')
#     USERNAME_FIELD = 'username'

#     def __str__(self):
#         return self.full_name
    
#     class Meta:
#         verbose_name = "User"
#         verbose_name_plural = "User"

    

#     @property
#     def tokens(self):
#         refresh = RefreshToken.for_user(self)
#         data = {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token)
#         }
#         return data


# class Chat(models.Model):
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chat_sender")
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chat_receiver")
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)


# ####
# from django.core.validators import RegexValidator
# from django.db import models
# from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
# from django.utils.translation import gettext_lazy as _
# from rest_framework_simplejwt.tokens import RefreshToken


# class UserManager(BaseUserManager):
#     """Manager for users."""

#     def create_user(self, email, password=None, **extra_fields):
#         """Create, save, and return a new user."""
#         if not email:
#             raise ValueError('User must have an email address.')

#         user = self.model(email=self.normalize_email(email), **extra_fields)
#         user.set_password(password)
#         user.full_clean()  # Validate model fields
#         user.save(using=self._db)

#         return user

#     def create_superuser(self, email, password, **extra_fields):
#         """Create and return a new superuser."""
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)


# class User(AbstractUser):
#     USER_TYPE_CHOICES = (
#         ('admin', 'Admin'),
#         ('user', 'User')
#     )

#     user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=20)
#     phone_regex = RegexValidator(
#         regex=r'^\+?1?\d{9,15}$',
#         message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
#     )
#     phone_number = models.CharField(max_length=20, validators=[phone_regex])
#     full_name = models.CharField(max_length=255)
#     username = models.CharField(max_length=255, unique=True)

#     objects = UserManager()
#     groups = models.ManyToManyField(Group, blank=True, related_name='users')
#     USERNAME_FIELD = 'username'

#     def __str__(self):
#         return self.full_name

#     @property
#     def tokens(self):
#         refresh = RefreshToken.for_user(self)
#         return {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token)
#         }

#     def clean(self):
#         super().clean()
#         if self.user_type == 'admin' and not self.is_superuser:
#             raise models.ValidationError(_('Only superusers can have the user_type set to "admin".'))


# class Chat(models.Model):
#     sender = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="sent_chats"
#     )
#     receiver = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="received_chats"
#     )
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Chat #{self.id} - From: {self.sender} To: {self.receiver}"

#     def clean(self):
#         super().clean()
#         if self.sender == self.receiver:
#             raise models.ValidationError(_('Sender and receiver cannot be the same user.'))



from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save, and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and return a new superuser."""
        extra_fields.setdefault('is_staff', True)   
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User')
    )

    user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=20)
    phone_number = models.CharField(max_length=20)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    objects = UserManager()
    groups = models.ManyToManyField(Group, blank=True, related_name='users')
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.full_name

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


class Chat(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_chats"
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="received_chats"
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat #{self.id} - From: {self.sender} To: {self.receiver}"

