from django.contrib.auth.models import AbstractUser
from django.db import models
from users.models.managers import MyUserManager


class User(AbstractUser):

    email = models.EmailField(
        verbose_name="email address",
        max_length=192,
        unique=True
    )
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    last_login = None

    # Доп поля для модели "Пользователь"
    about_me = models.CharField(max_length=1500, blank=True, )
    at_registration = models.DateTimeField(auto_now_add=True)  # Дата регистрации "Пользователя"

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'