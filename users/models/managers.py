from django.contrib.auth.base_user import BaseUserManager

class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def new_create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a user with the given email and password.
        """
        extra_fields.setdefault('is_admin', False)
        extra_fields.setdefault('is_active', True)


        return self.new_create_user(
            email,
            password=password,
            **extra_fields
        )

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)

        return self.new_create_user(
            email,
            password=password,
            **extra_fields
        )