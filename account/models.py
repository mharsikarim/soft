from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
    def create_user(self, email,nom_societe,adress,numero_telephone, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nom_societe=nom_societe,
            adress=adress,
            numero_telephone=numero_telephone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password,numero_telephone,adress,nom_societe):
        user = self.create_user(
            email,
            password=password,
            numero_telephone=numero_telephone,
            adress=adress,
            nom_societe=nom_societe,

        )
        user.is_admin= True
        user.is_client= True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    nom_societe= models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    numero_telephone =models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_client = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom_societe','numero_telephone','adress']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin